import math

import pandas as pd


def LikeBot(facebookDF):
    subsetDF = facebookDF.loc[
        (facebookDF['likes'] > 0) & (facebookDF['likes_received'] > 0) & (facebookDF['friend_count'] > 0), ('userid', 'likes', 'likes_received', 'friend_count')]
    subsetDF['likeBot'] = subsetDF.apply(LikeBotRanking, axis=1)
    return subsetDF


def fakestFriend(facebookDF):
    subsetDF = facebookDF.loc[
        (facebookDF['likes'] > 0) & (facebookDF['friend_count'] > 0) & (facebookDF['friendships_initiated'] > 0), ('userid', 'likes', 'friend_count', 'friendships_initiated')]
    subsetDF['fakestFriend'] = subsetDF.apply(fakeFriendRanking, axis=1)

    return subsetDF


def LikeBotRanking(row):
    rank = row['likes'] / (row['likes_received'] + 1) + (row['friend_count']/500)

    return rank

def friendliness(row):
    rank = row['friendships_initiated'] / (row['friend_count']+1)
    return rank

def fakeFriendRanking(row):
    rank = (row['friend_count']) / (row['likes'] + 1) + row['friendships_initiated'] / (row['friend_count'] + 1)

    return rank


def nSmallest(facebookDF, n, queryAttr):
    df = facebookDF.nsmallest(n, queryAttr)

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

def influenceRanking(row):
    return row['likes_received'] / (row['friend_count'] + 1)

class KNN:
    def __init__(self):
        self.subsetDFTrain = pd.read_csv('data/pseudo_facebook.csv')

    def label(self, facebookDF):
        subsetDF = facebookDF
        subsetDF['likeBot'] = subsetDF.apply(LikeBotRanking, axis=1)
        subsetDF['fakestFriend'] = subsetDF.apply(fakeFriendRanking, axis=1)
        subsetDF['friendliness'] = subsetDF.apply(friendliness, axis=1)
        subsetDF['influence'] = subsetDF.apply(influenceRanking, axis=1)
        l_ist = []

        for row in subsetDF.iterrows():
            maxL = [(row[1]['likeBot'], 'Like Bot'), (row[1]['fakestFriend'], 'Fake Friend'),
                    (row[1]['friendliness'], 'Friendly'),(row[1]['influence'], 'Influencer')]
            spot = maxL.index(max(maxL))
            label = maxL[spot][1]
            l_ist.append(label)
        subsetDF['label'] = l_ist
        self.subsetDFTrain = subsetDF

    def predict(self, listUser):
        similarity = []
        for row in self.subsetDFTrain.iterrows():
            top = 0.0
            bota = 0.0
            botb = 0.0
            count = 0
            for item in listUser:
                if count != 0:

                    top += row[1][item[1]] * item[0]
                    bota += pow(item[0], 2)
                count = count + 1
            count = 0
            #print("Row: ", row)
            for a in row[1]:
                if count != 0:
                    if isinstance(a, int):
                        #print("a: ", a)
                        botb += pow(a, 2)
                count = count + 1
            s = top / (math.sqrt(bota) * math.sqrt(botb))
            similarity.append((s, row[1]['label']))
        n_doc = {}
        largestVal = 0
        largestLabel = ""
        print("Labels of most similar users")
        for i in range(5):
            spot = similarity.index(max(similarity))
            label = similarity[spot][1]
            print(label)
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
