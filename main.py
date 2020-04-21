import pandas as pd
from utils import *
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
