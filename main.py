import pandas as pd
from utils import *


if __name__ == "__main__":
    facebookDF = pd.read_csv('data/pseudo_facebook.csv')

    print(mostLikedUser(facebookDF))
    print(mostLikesHandedOut(facebookDF))
    print(friendliestGuy(facebookDF))
    print(guyEveryoneWantsToKnow(facebookDF))
    print(longestTimeOnFacebook(facebookDF))
    print(leastLikedUser(facebookDF))
    print(leastLikesHandedOut(facebookDF))
    print(unfriendliestGuy(facebookDF))
    print(guyNobodyWantsToKnow(facebookDF))
    print(shortestTimeOnFacebook(facebookDF))

    print(nLargest(facebookDF, 3, 'likes_received'))
