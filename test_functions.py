import math
import pandas as pd


def fakestUser(facebookDF):
    print("FAKEST USER")

    subsetDF = facebookDF.loc[
        (facebookDF['likes'] > 0) & (facebookDF['likes_received'] > 0), ('userid', 'likes', 'likes_received')]
    subsetDF['fakestUser'] = subsetDF.apply(fakeUserRanking, axis=1)
    return subsetDF


def fakestFriend(facebookDF):
    print("FAKEST FRIEND")

    subsetDF = facebookDF.loc[
        (facebookDF['likes'] > 0) & (facebookDF['friend_count'] > 0), ('userid', 'likes', 'friend_count')]
    subsetDF['fakestFriend'] = subsetDF.apply(fakeFriendRanking, axis=1)
    print(subsetDF)
    return subsetDF


def fakeUserRanking(row):
    rank = row['likes'] / (row['likes_received'] + 1)

    return rank


def fakeFriendRanking(row):
    rank = (row['friend_count']) / (row['likes'] + 1)

    return rank


def nSmallest(facebookDF, n, queryAttr):
    df = facebookDF.nsmallest(n, queryAttr)
    print(df)
    userids = []
    attribute = []
    for index, row in df.iterrows():
        userids.append(row['userid'])
        attribute.append(row[queryAttr])

    return {'userid': userids, queryAttr: attribute}


def desktopUser(facebookDF, userID):
    a = facebookDF.loc[facebookDF['userid'] == userID]
    if a['mobile_likes'].item() - a['www_likes'].item() < 0:
        return True
    return False


class KNN:
    def __init__(self):
        self.subsetDFTrain = pd.read_csv('data/pseudo_facebook.csv')

    def train(self, facebookDF):
        subsetDF = facebookDF
        subsetDF['fakestUser'] = subsetDF.apply(fakeUserRanking, axis=1)
        subsetDF['fakestFriend'] = subsetDF.apply(fakeFriendRanking, axis=1)
        l_ist = []
        for row in subsetDF.iterrows():
            if row[1]['fakestUser'] > row[1]['fakestFriend']:
                l_ist.append("fakestUser")
            else:
                l_ist.append("fakestFriend")
        subsetDF['label'] = l_ist
        self.subsetDFTrain = subsetDF
        print(subsetDF)

    def predict(self, listUser):
        similarity = []
        for row in self.subsetDFTrain.iterrows():
            top = 0.0
            bota = 0.0
            botb = 0.0
            for item in listUser:
                top += row[1][item[1]] * item[0]
                bota += pow(item[0], 2)
            for a in row[1]:
                if isinstance(a, int):
                    botb += pow(a, 2)
            s = top / (math.sqrt(bota) * math.sqrt(botb))
            similarity.append((s, row[1]['label']))
        n_doc = {}
        largestVal = 0
        largestLabel = ""
        for i in range(5):
            spot = similarity.index(max(similarity))
            label = similarity[spot][1]
            if n_doc.get(label) is not None:
                n = n_doc.get(label)
                n += 1
                if n > largestVal:
                    largestLabel = label
                    largestVal = n
                n_doc.update({label: n})
            else:
                if 1 > largestVal:
                    largestLabel = label
                    largestVal = 1
                n_doc.update({label: 1})
            similarity.remove(max(similarity))

        return largestLabel
