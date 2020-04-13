from builtins import int, round, max, range, len, abs, min

import pandas


def topDoppelPairs(facebookDF, n):

    contenders = facebookDF.loc[(facebookDF['likes_received'] > 2250) & (facebookDF['friend_count'] > 3250), ('userid', 'friend_count', 'friendships_initiated', 'likes', 'likes_received', 'age', 'tenure', 'gender')]

    # error checking (don't return more scores than there are contenders)
    if n > len(contenders):
        n = len(contenders)

    doppelScores = []
    for index, row in contenders.iterrows():
        for index2, row2 in contenders.iterrows():
            if index != index2:
                continueCheck = True
                for duo in doppelScores:
                    if (duo[3] == index and duo[4] == index2) or (duo[3] == index2 and duo[4] == index):
                        continueCheck = False
                        break
                if continueCheck is True:
                    doppelScores.append([row, row2, 0, index, index2])

    for duo in doppelScores:
        doppelScore = computeDoppelScore(duo[0], duo[1])
        duo[2] = doppelScore
        duo.pop(3)
        duo.pop(3)

    topScorers = []
    for i in range(0, n):
        scoreList = []
        for triplet in doppelScores:
            scoreList.append(triplet[2])
        maxScore = max(scoreList)
        for triplet in doppelScores:
            if triplet[2] == maxScore:
                topScorers.append([triplet[0], triplet[1], triplet[2]])
                triplet[2] = 0
                break

    # print(user)

    for scorer in topScorers:
        scorer[0] = {'userid': (scorer[0]['userid'])}
        scorer[1] = {'userid': (scorer[1]['userid'])}
        scorer[2] = {'doppelScore': scorer[2]}

    return topScorers


def computeDoppelScore(user1, user2):

    friendshipsInitiatedWeight = 0.08
    friendCountWeight = 0.08
    likesGivenWeight = 0.08
    likesReceivedWeight = 0.08
    genderWeight = 0.35
    ageWeight = 0.25
    tenureWeight = 0.08

    doppelScore = 0.0

    friendshipsInitiatedScore = 0.0
    friendCountScore = 0.0
    likesGivenScore = 0.0
    likesReceivedScore = 0.0
    genderScore = 0.0
    ageScore = 0.0
    tenureScore = 0.0

    if (user1['friendships_initiated'] - user2['friendships_initiated']) == 0:
        friendshipsInitiatedScore = 1.0
    else:
        friendshipsInitiatedScore = abs(1 / (user1['friendships_initiated'] - user2['friendships_initiated']))

    if (user1['friend_count'] - user2['friend_count']) == 0:
        friendCountScore = 1.0
    else:
        friendCountScore = abs(1 / (user1['friend_count'] - user2['friend_count']))

    if (user1['likes_received'] - user2['likes_received']) == 0:
        likesReceivedScore = 1.0
    else:
        likesReceivedScore = abs(1 / (user1['likes_received'] - user2['likes_received']))

    if (user1['likes'] - user2['likes']) == 0:
        likesGivenScore = 1.0
    else:
        likesGivenScore = abs(1 / (user1['likes'] - user2['likes']))

    if user1['gender'] is user2['gender']:
        genderScore = 1.0
    else:
        genderScore = 0.0

    if (user1['age'] - user2['age']) == 0:
        ageScore = 1.0
    else:
        ageScore = abs(1 / (user1['age'] - user2['age']))

    if (user1['tenure'] - user2['tenure']) == 0:
        tenureScore = 1.0
    else:
        tenureScore = abs(1 / (user1['tenure'] - user2['tenure']))

    doppelScore = friendshipsInitiatedScore * friendshipsInitiatedWeight + friendCountScore * friendCountWeight + likesGivenScore * likesGivenWeight + likesReceivedScore * likesReceivedWeight + genderScore * genderWeight + ageScore * ageWeight + tenureScore * tenureWeight

    return doppelScore


def specificScore(user1, user2, facebookDF):

    triplet = []
    contenders = facebookDF.loc[(facebookDF['userid'] == user1) | (facebookDF['userid'] == user2), ('userid', 'friend_count', 'friendships_initiated', 'likes', 'likes_received', 'age', 'tenure', 'gender')]
    for index, row in contenders.iterrows():
        triplet.append(row)
    triplet.append(0)
    doppelScore = computeDoppelScore(triplet[0], triplet[1])
    triplet[0] = {'userid': (triplet[0]['userid'])}
    triplet[1] = {'userid': (triplet[1]['userid'])}
    triplet[2] = {'doppelScore': doppelScore}
    return triplet


def findDoppelganger(user, facebookDF):

    suspects = []
    contenders = facebookDF.loc[(facebookDF['userid'] != user) & (facebookDF['likes_received'] > 1000) & (facebookDF['friend_count'] > 1500), ('userid', 'friend_count', 'friendships_initiated', 'likes', 'likes_received', 'age', 'tenure', 'gender')]
    for index, row in contenders.iterrows():
        for indexMe, rowMe in facebookDF.loc[facebookDF['userid'] == user, ('userid', 'friend_count', 'friendships_initiated', 'likes', 'likes_received', 'age', 'tenure', 'gender')].iterrows():
            suspects.append([rowMe, row, 0])

    for duo in suspects:
        doppelScore = computeDoppelScore(duo[0], duo[1])
        duo[2] = doppelScore

    scoreList = []
    for triplet in suspects:
        scoreList.append(triplet[2])
    maxScore = max(scoreList)
    for triplet in suspects:
        if triplet[2] == maxScore:
            triplet[0] = {'userid': (triplet[0]['userid'])}
            triplet[1] = {'userid': (triplet[1]['userid'])}
            triplet[2] = {'doppelScore': triplet[2]}
            return triplet


def findOpposite(user, facebookDF):

    suspects = []
    contenders = facebookDF.loc[(facebookDF['userid'] != user) & (facebookDF['likes_received'] > 1000) & (facebookDF['friend_count'] > 1500), ('userid', 'friend_count', 'friendships_initiated', 'likes', 'likes_received', 'age', 'tenure', 'gender')]
    for index, row in contenders.iterrows():
        for indexMe, rowMe in facebookDF.loc[facebookDF['userid'] == user, ('userid', 'friend_count', 'friendships_initiated', 'likes', 'likes_received', 'age', 'tenure', 'gender')].iterrows():
            suspects.append([rowMe, row, 0])

    for duo in suspects:
        doppelScore = computeDoppelScore(duo[0], duo[1])
        duo[2] = doppelScore

    scoreList = []
    for triplet in suspects:
        scoreList.append(triplet[2])
    minScore = min(scoreList)
    for triplet in suspects:
        if triplet[2] == minScore:
            triplet[0] = {'userid': (triplet[0]['userid'])}
            triplet[1] = {'userid': (triplet[1]['userid'])}
            triplet[2] = {'doppelScore': triplet[2]}
            return triplet


def topOpposites(facebookDF, n):

    contenders = facebookDF.loc[(facebookDF['likes_received'] > 2250) & (facebookDF['friend_count'] > 3250), ('userid', 'friend_count', 'friendships_initiated', 'likes', 'likes_received', 'age', 'tenure', 'gender')]

    # error checking (don't return more scores than there are contenders)
    if n > len(contenders):
        n = len(contenders)

    doppelScores = []
    for index, row in contenders.iterrows():
        for index2, row2 in contenders.iterrows():
            if index != index2:
                continueCheck = True
                for duo in doppelScores:
                    if (duo[3] == index and duo[4] == index2) or (duo[3] == index2 and duo[4] == index):
                        continueCheck = False
                        break
                if continueCheck is True:
                    doppelScores.append([row, row2, 0, index, index2])

    for duo in doppelScores:
        doppelScore = computeDoppelScore(duo[0], duo[1])
        duo[2] = doppelScore
        duo.pop(3)
        duo.pop(3)

    topScorers = []
    for i in range(0, n):
        scoreList = []
        for triplet in doppelScores:
            scoreList.append(triplet[2])
        minScore = min(scoreList)
        for triplet in doppelScores:
            if triplet[2] == minScore:
                topScorers.append([triplet[0], triplet[1], triplet[2]])
                triplet[2] = 1.0
                break

    for scorer in topScorers:
        scorer[0] = {'userid': (scorer[0]['userid'])}
        scorer[1] = {'userid': (scorer[1]['userid'])}
        scorer[2] = {'doppelScore': scorer[2]}

    return topScorers
