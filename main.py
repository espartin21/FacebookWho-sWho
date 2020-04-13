import pandas as pd
from utils import *
from influential import *
from doppel import *

if __name__ == "__main__":

    facebookDF = pd.read_csv('../data/pseudo_facebook.csv')

    # print(mostLikedUser(facebookDF))
    # print(mostLikesHandedOut(facebookDF))
    # print(friendliestGuy(facebookDF))
    # print(guyEveryoneWantsToKnow(facebookDF))
    # print(longestTimeOnFacebook(facebookDF))
    # print(leastLikedUser(facebookDF))
    # print(leastLikesHandedOut(facebookDF))
    # print(unfriendliestGuy(facebookDF))
    # print(guyNobodyWantsToKnow(facebookDF))
    # print(shortestTimeOnFacebook(facebookDF))

    # print(nLargest(facebookDF, 3, 'likes_received'))

    # print(mostInfluential(facebookDF))

    # compute top 'n' celebrity doppelganger pairs
    '''
    n = 5
    picks = topDoppelPairs(facebookDF, n)
    for pick in picks:
        print(pick)
    '''

    # compute doppelScore for 2 arbitrary users
    '''
    userID1 = 2150204
    userID2 = 1565349
    print(specificScore(userID1, userID2, facebookDF))
    '''

    # find a celebrity doppelganger for an arbitrary user
    '''
    userID = 1066459
    print(findDoppelganger(userID, facebookDF))
    '''

    # find a celebrity opposite for an arbitrary user
    '''
    userID = 1066459
    print(findOpposite(userID, facebookDF))
    '''

    # compute top 'n' celebrity polar opposites
    '''
    n = 5
    picks = topOpposites(facebookDF, n)
    for pick in picks:
        print(pick)
    '''
