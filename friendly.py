import pandas


def findFriendliness(row):
    if (row['friendships_initiated'] / row['friend_count'] > 0.85):
        return 1
    elif (row['friendships_initiated'] / row['friend_count'] < 0.15):
        return -1
    else:
        return 0


def friendly(facebookDF):
    subsetDF = facebookDF.loc[(facebookDF['friend_count'] > 0) & (
        facebookDF['friendships_initiated'] > 0), ['userid', 'friend_count', 'friendships_initiated']]

    subsetDF['friendly'] = subsetDF.apply(findFriendliness, axis=1)

    return subsetDF


def areYouFriendly(friendlyDF, userID):
    f = friendlyDF.loc[friendlyDF['userid'] == userID]

    return int(f.iloc[0]['friendly'])
