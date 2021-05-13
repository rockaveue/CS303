from math import exp
from numpy import unique
from numpy import where
import numpy as np
from sklearn.datasets import make_classification
from matplotlib import pyplot
import random
import sys

# Зай олох функц
def getDistance(x1,x2,y1,y2):
    #manhattan
    return abs(x1 - x2) + abs(y1 - y2)
    #euclid    
    # return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    #cosine
    # return 1 - (x1 * y1 + x2 * y2) / (((x1 ** 2 + x2 ** 2) ** 0.5) * ((y1 ** 2 + y2 ** 2) ** 0.5))
# Датасетыг тодорхойлох
X, _ = make_classification(n_samples=1000, n_features=2,
n_informative=2, n_redundant=0, n_clusters_per_class=1,
random_state=4)

print(f"Нийт цэгийн тоо: {len(X)}")

# cluster uusgeh
clusters = [0, 1, 2, 3, 4]
clusters = unique(clusters)
# Нийт итераци хийх тоо оруулах хувьсагч
k = 20
print(f"нийт давталт: {k}")
print(f"clusters: {clusters}")
# centroid байх хувьсагч
centroids = []
# anhnii cluster random
for i in clusters:
    # sanamsarguigeer centroid songov
    centroids.append(X[random.randint(0, len(X)-1)])
# k тоогоор давтах давталт
for j in range(k):
    # yhat baih huvisagch
    map = []
    # buh tseguudiin davtalt
    for dots in X:
        # tuhain tsegiin zainuud hadgalah list
        distance = []
        # centroid buriin davtalt
        for centroid in centroids:
            # zai olj baigaa heseg
            dist = getDistance(dots[0], centroid[0], centroid[1], dots[1])
            # tuhain tsegiin centroid buriin zaig hiij baina
            distance.append(dist)
        # hamgiin oiriin centroid iig songov
        minDistance = min(distance)
        # tuhain centroid-iin clusters dah toog map-d hiiv
        map.append(distance.index(minDistance))
        # # hamgiin suuliin index baival
    # centroid shinechleh
    for cluster in clusters:
        # niilber hadgalah huvisagchid
        sumX = 0
        sumY = 0
        # huuchin centroid oor olson mapaas indexuudiig avav
        clusInd = where(map == cluster)
        # centroid shinechlegdehed ashiglagdah clusterd hamaarah vectoriin niilber oloh davtalt
        for i in clusInd[0]:
            sumX += X[i][0]
            sumY += X[i][1]
        # tuhain medianuudiig shine centroid bolgov
        centroids[cluster][0] = sumX / len(clusInd[0])
        centroids[cluster][1] = sumY / len(clusInd[0])

print(f"Centroids: {centroids}")
# matplotlib-eer haruulah
for cluster in clusters:
    # map-aas tseguudtei hamaarulj cluster buriin index-iig avav
    row_ix = where(map == cluster)
    # avsan indextei huvisagchiig plot deeree oruulav
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    
pyplot.show()
