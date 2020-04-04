import pandas


def mostLikedUser(facebookDF):
    df = facebookDF[facebookDF.likes_received ==
                    facebookDF['likes_received'].max()]

    return {'userid': (int)(df.iloc[0]['userid']), 'likes_received': (int)(df.iloc[0]['likes_received'])}


def mostLikesHandedOut(facebookDF):
    df = facebookDF[facebookDF.likes == facebookDF['likes'].max()]

    return {'userid': (int)(df.iloc[0]['userid']), 'likes': (int)(df.iloc[0]['likes'])}


def friendliestGuy(facebookDF):
    df = facebookDF[facebookDF.friendships_initiated ==
                    facebookDF['friendships_initiated'].max()]

    return {'userid': (int)(df.iloc[0]['userid']), 'friendships_initiated': (int)(df.iloc[0]['friendships_initiated'])}


def guyEveryoneWantsToKnow(facebookDF):
    df = facebookDF[facebookDF.friend_count ==
                    facebookDF['friend_count'].max()]

    return {'userid': (int)(df.iloc[0]['userid']), 'friend_count': (int)(df.iloc[0]['friend_count'])}


def longestTimeOnFacebook(facebookDF):
    df = facebookDF[facebookDF.tenure == facebookDF['tenure'].max()]

    return {'userid': (int)(df.iloc[0]['userid']), 'tenure': (int)(df.iloc[0]['tenure'])}


def leastLikedUser(facebookDF):
    df = facebookDF[facebookDF.likes_received ==
                    facebookDF['likes_received'].min()]

    return {'userid': (int)(df.iloc[0]['userid']), 'likes_received': (int)(df.iloc[0]['likes_received'])}


def leastLikesHandedOut(facebookDF):
    df = facebookDF[facebookDF.likes == facebookDF['likes'].min()]

    return {'userid': (int)(df.iloc[0]['userid']), 'likes': (int)(df.iloc[0]['likes'])}


def unfriendliestGuy(facebookDF):
    df = facebookDF[facebookDF.friendships_initiated ==
                    facebookDF['friendships_initiated'].min()]

    return {'userid': (int)(df.iloc[0]['userid']), 'friendships_initiated': (int)(df.iloc[0]['friendships_initiated'])}


def guyNobodyWantsToKnow(facebookDF):
    df = facebookDF[facebookDF.friend_count ==
                    facebookDF['friend_count'].min()]

    return {'userid': (int)(df.iloc[0]['userid']), 'friend_count': (int)(df.iloc[0]['friend_count'])}


def shortestTimeOnFacebook(facebookDF):
    df = facebookDF[facebookDF.tenure == facebookDF['tenure'].min()]

    return {'userid': (int)(df.iloc[0]['userid']), 'tenure': (int)(df.iloc[0]['tenure'])}


def nLargest(facebookDF, n, queryAttr):
    df = facebookDF.nlargest(n, queryAttr)

    userids = []
    attribute = []
    for index, row in df.iterrows():
        userids.append(row['userid'])
        attribute.append(row[queryAttr])

    return {'userid': userids, queryAttr: attribute}
