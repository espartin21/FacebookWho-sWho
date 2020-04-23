import pandas as pd
from utils import *
from doppel import *
from activity import *
from test_functions import *
from influential import *
from friendly import *

if __name__ == "__main__":
    facebookDF = pd.read_csv('data/pseudo_facebook.csv')

    print("Finding most liked user...")
    print(mostLikedUser(facebookDF))
    print('\n')

    print("Finding user with most likes handed out...")
    print(mostLikesHandedOut(facebookDF))
    print('\n')

    print("Finding friendliest guy...")
    print(friendliestGuy(facebookDF))
    print('\n')

    print("Finding user everyone wants to know...")
    print(guyEveryoneWantsToKnow(facebookDF))
    print('\n')

    print("Finding user with longest tenure on facebook...")
    print(longestTimeOnFacebook(facebookDF))
    print('\n')

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

    influentialDF = mostInfluential(facebookDF)
    print("Top 3 most influential users:")
    print(nLargest(influentialDF, 3, 'influence'))
    print('\n')

    upAndComers = mostInfluential(
        facebookDF[facebookDF['tenure'] < facebookDF['tenure'].mean() - 100])
    print("Top 3 most influential up and comers:")
    print(nLargest(upAndComers, 3, 'influence'))
    print('\n')

    fakeDF = LikeBot(facebookDF)
    print("Top 3 Like Bots: ")
    print(nLargest(fakeDF, 3, 'likeBot'))
    print('\n')

    fakeDF = fakestFriend(facebookDF)
    print("Top 3 Fakest Friends: ")
    print(nLargest(fakeDF, 3, 'fakestFriend'))
    print('\n')

    friendlyDF = friendly(facebookDF)
    userid = 1654565
    friendlyClassifier = areYouFriendly(friendlyDF, userid)
    print("Finding out if user " + str(userid) +
          " is friendly, unfriendly, or between...")
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
    knn.label(facebookDF)
    # a = [(2098916, 'userid'), (69, 'age'), (2, 'dob_day'), (1944, 'dob_year'), (10, 'dob_month'), (506, 'tenure'), (1, 'friend_count'),
    #     (23, 'friendships_initiated'), (32, 'likes'), (114, 'likes_received'), (29, 'mobile_likes'), (49, 'mobile_likes_received'), (3, 'www_likes'), (65, 'www_likes_received')]

    a = [(1364866, 'userid'), (18, 'age'), (22, 'dob_day'), (1995, 'dob_year'), (5, 'dob_month'), (279, 'tenure'),
         (27, 'friend_count'),
         (21, 'friendships_initiated'), (25, 'likes'), (39,
                                                        'likes_received'), (22, 'mobile_likes'),
         (26, 'mobile_likes_received'), (3, 'www_likes'), (13, 'www_likes_received')]
    print("Predicting what label user " + str(a[0][0]) + " belongs too...")
    print("User " + str(a[0][0]) + " is a " + knn.predict(a))
