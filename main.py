import pandas as pd
from utils import *
from test_functions import *

if __name__ == "__main__":
    facebookDF = pd.read_csv('data/pseudo_facebook.csv')
    #fakeDF = fakestUser(facebookDF)
    #print(nLargest(fakeDF, 3, 'fakestUser'))
    #fakeDF = fakestFriend(facebookDF)
    #print(nLargest(fakeDF, 3, 'fakestFriend'))
    knn = KNN()
    knn.train(facebookDF)
    a = [(2098916,'userid'),(69,'age'),(2,'dob_day'),(1944,'dob_year'),(10,'dob_month'),(506,'tenure'),(54,'friend_count'),
        (23,'friendships_initiated'),(32,'likes'),(114,'likes_received'),(29,'mobile_likes'),(49,'mobile_likes_received'),(3,'www_likes'),(65,'www_likes_received')]
    print(knn.predict(a))
    id = 1270630
    if desktopUser(facebookDF, id):
        print("User: " + str(id) + " is a desktop user")
    else:
        print("User: " +str(id) + " is a mobile user")
    #print(mostLikedUser(facebookDF))
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
