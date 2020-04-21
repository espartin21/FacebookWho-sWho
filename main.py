import pandas as pd
from utils import *
from doppel import *
from activity import *
from test_functions import *
from influential import *
from friendly import *

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

    # Queries
    influentialDF = mostInfluential(facebookDF)
    print("Top 3 most influential users:")
    print(nLargest(influentialDF, 3, 'influence'))
    print('\n')

    upAndComers = mostInfluential(
        facebookDF[facebookDF['tenure'] < facebookDF['tenure'].mean() - 100])
    print("Top 3 most influential up and comers:")
    print(nLargest(upAndComers, 3, 'influence'))
    print('\n')

    fakeDF = fakestUser(facebookDF)
    print("Top 3 Fakest Users: ")
    print(nLargest(fakeDF, 3, 'fakestUser'))
    print('\n')

    fakeDF = fakestFriend(facebookDF)
    print("Top 3 Fakest Friends: ")
    print(nLargest(fakeDF, 3, 'fakestFriend'))
    print('\n')

    # Classifiers
    friendlyDF = friendly(facebookDF)
    userid = 1654565
    friendlyClassifier = areYouFriendly(friendlyDF, userid)
    if friendlyClassifier == 1:
        print("User " + str(userid) + " is super friendly!")
    elif friendlyClassifier == -1:
        print("User " + str(userid) + " is super unfriendly!")
    elif friendlyClassifier == 0:
        print("User " + str(userid) + " is somewhere in between!")
    print('\n')

    id = 1270630
    if desktopUser(facebookDF, id):
        print("User " + str(id) + " is a desktop user")
    else:
        print("User " + str(id) + " is a mobile user")
    print('\n')

    knn = KNN()
    knn.train(facebookDF)
    a = [(2098916, 'userid'), (69, 'age'), (2, 'dob_day'), (1944, 'dob_year'), (10, 'dob_month'), (506, 'tenure'), (54, 'friend_count'),
         (23, 'friendships_initiated'), (32, 'likes'), (114, 'likes_received'), (29, 'mobile_likes'), (49, 'mobile_likes_received'), (3, 'www_likes'), (65, 'www_likes_received')]
    print("Prediciting what label user " + str(a[0][0]) + " belongs too...")
    print("User " + str(a[0][0]) + " is a " + knn.predict(a))
