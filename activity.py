from builtins import int, round, max, range, len, abs, min

import pandas


def isHighlyActive(facebookDF, userID):

    # find the specified user
    user = None
    person = facebookDF.loc[facebookDF['userid'] == userID, ('userid', 'friendships_initiated', 'likes', 'tenure')]
    for index, row in person.iterrows():
        user = row

    likesActive = False
    friendsActive = False
    highlyActive = False

    likesGivenScore = 0.0
    friendshipsInitiatedScore = 0.0

    # compute the amount of likes given per day
    if user['tenure'] == 0:
        likesGivenScore = 0
    else:
        likesGivenScore = user['likes'] / user['tenure']
    if likesGivenScore >= 2.5:
        likesActive = True

    # compute the amount of friendships initiated per day
    if user['tenure'] == 0:
        friendshipsInitiatedScore = 0
    else:
        friendshipsInitiatedScore = user['friendships_initiated'] / user['tenure']
    if friendshipsInitiatedScore >= 0.75:
        friendsActive = True

    if friendsActive | likesActive:
        highlyActive = True

    return highlyActive


def isHighlyInactive(facebookDF, userID):

    # find the specified user
    user = None
    person = facebookDF.loc[facebookDF['userid'] == userID, ('userid', 'friendships_initiated', 'likes', 'tenure')]
    for index, row in person.iterrows():
        user = row

    likesInactive = False
    friendsInactive = False
    highlyInactive = False

    likesGivenScore = 0.0
    friendshipsInitiatedScore = 0.0

    # compute the amount of likes given per day
    if user['tenure'] == 0:
        likesGivenScore = 0
    else:
        likesGivenScore = user['likes'] / user['tenure']
    if likesGivenScore <= 0.005:
        likesInactive = True

    # compute the amount of friendships initiated per day
    if user['tenure'] == 0:
        friendshipsInitiatedScore = 0
    else:
        friendshipsInitiatedScore = user['friendships_initiated'] / user['tenure']
    if friendshipsInitiatedScore <= 0.01:
        friendsInactive = True

    if friendsInactive | likesInactive:
        highlyInactive = True

    return highlyInactive
