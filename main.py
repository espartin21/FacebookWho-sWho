import pandas as pd


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


if __name__ == "__main__":
    facebookDF = pd.read_csv('data/pseudo_facebook.csv')

    mostLiked = mostLikedUser(facebookDF)
    mostLikesGiven = mostLikesHandedOut(facebookDF)
    friendly = friendliestGuy(facebookDF)
    coolestCat = guyEveryoneWantsToKnow(facebookDF)
    alwaysOnline = longestTimeOnFacebook(facebookDF)

    print(mostLiked)
    print(mostLikesGiven)
    print(friendly)
    print(coolestCat)
    print(alwaysOnline)
