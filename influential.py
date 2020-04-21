import pandas


def findWeightedInfluence(row):
    weightFactor = (row['friend_count'] / 100) * 0.1

    return round(((row['likes_received'] / row['friend_count']) * (row['friend_count'] * weightFactor)), 2)


def mostInfluential(facebookDF):
    subsetDF = facebookDF.loc[(facebookDF['likes_received'] > 0) &
                              (facebookDF['friend_count'] > 0), ('userid', 'friend_count', 'likes_received')]

    subsetDF['influence'] = subsetDF.apply(findWeightedInfluence, axis=1)

    return subsetDF
