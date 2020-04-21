import pandas as pd
from utils import *
from test_functions import *
from influential import *
from friendly import *

if __name__ == "__main__":
    facebookDF = pd.read_csv('data/pseudo_facebook.csv')

    # Queries
    influentialDF = mostInfluential(facebookDF)
    print(nLargest(influentialDF, 3, 'influence'))

    upAndComers = mostInfluential(
        facebookDF[facebookDF['tenure'] < facebookDF['tenure'].mean() - 100])
    print(nLargest(upAndComers, 3, 'influence'))
    
    fakeDF = fakestUser(facebookDF)
    print("Top 3 Fakest Users: ")
    print(nLargest(fakeDF, 3, 'fakestUser'))

    fakeDF = fakestFriend(facebookDF)
    print("Top 3 Fakest Friends: ")
    print(nLargest(fakeDF, 3, 'fakestFriend'))

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
        
    id = 1270630
    if desktopUser(facebookDF, id):
        print("User: " + str(id) + " is a desktop user")
    else:
        print("User: " + str(id) + " is a mobile user")
        
    knn = KNN()
    knn.train(facebookDF)
    a = [(2098916, 'userid'), (69, 'age'), (2, 'dob_day'), (1944, 'dob_year'), (10, 'dob_month'), (506, 'tenure'), (54, 'friend_count'),
         (23, 'friendships_initiated'), (32, 'likes'), (114, 'likes_received'), (29, 'mobile_likes'), (49, 'mobile_likes_received'), (3, 'www_likes'), (65, 'www_likes_received')]
    print(knn.predict(a))
