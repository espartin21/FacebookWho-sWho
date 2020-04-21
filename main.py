import pandas as pd
from utils import *
from doppel import *
from activity import *

if __name__ == "__main__":

    facebookDF = pd.read_csv('data/pseudo_facebook.csv')

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
    n = 5
    picks = topDoppelPairs(facebookDF, n)
    print("Compute top 'n' celebrity doppelganger pairs")
    for pick in picks:
        print(pick)
    print('\n')

    # compute doppelScore for 2 arbitrary users
    userID1 = 2150204
    userID2 = 1565349
    print("Compute doppelScore for 2 arbitrary users")
    print(specificScore(userID1, userID2, facebookDF))
    print('\n')

    # find a celebrity doppelganger for an arbitrary user
    userID = 1066459
    print("Find a celebrity doppelganger for an arbitrary user")
    print(findDoppelganger(userID, facebookDF))
    print('\n')

    # find a celebrity opposite for an arbitrary user
    userID = 1066459
    print("Find a celebrity opposite for an arbitrary user")
    print(findOpposite(userID, facebookDF))
    print('\n')

    # compute top 'n' celebrity polar opposites
    n = 5
    picks = topOpposites(facebookDF, n)
    print("Compute top 'n' celebrity polar opposites")
    for pick in picks:
        print(pick)
    print('\n')

    # determine whether an arbitrary user is highly active
    userID = 1066459
    print("Determine whether user " + str(userID) + " is highly active")
    print(isHighlyActive(facebookDF, userID))
    print('\n')

    # determine whether an arbitrary user is highly inactive
    userID = 1646284
    print("Determine whether user " + str(userID) + " is highly inactive")
    print(isHighlyInactive(facebookDF, userID))
    print('\n')
