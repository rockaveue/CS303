# k-means ангилал
from math import exp
from numpy import unique
from numpy import where
import numpy as np
from sklearn.datasets import make_classification
from matplotlib import pyplot
import random
import sys

class GetOutOfLoop(Exception):
    pass
def getDistance(x1,x2,y1,y2):
    #manhattan
    # return abs(x1 - x2) + abs(y1 - y2)
    #euclid    
    return (abs(x1 - x2) ** 2 + abs(y1 - y2) ** 2) ** 0.5
    #cosine
    # return 1 - (x1 * y1 + x2 * y2) / (((x1 ** 2 + x2 ** 2) ** 0.5) * ((y1 ** 2 + y2 ** 2) ** 0.5))
# Датасетыг тодорхойлох
X, _ = make_classification(n_samples=1000, n_features=2,
n_informative=2, n_redundant=0, n_clusters_per_class=1,
random_state=4)
# print(X)
x = []
y = []
print(f"Нийт цэгийн тоо: {len(X)}")
# X deh datag x, y-t huvaaj hiiv
for i in range(len(X)):
    x.append(round(X[i][0], 4))
    y.append(round(X[i][1], 4))
    # print(i)
# X-iin data-g 1 hemjeest massiv bolgov
# dots = X.flatten()
# print(dots)
clusters = [0, 1, 2, 3 ,4]
clusters = unique(clusters)
k = 5
print(f"k: {k}")
print(f"clusters: {clusters}")
# yhat baih huvisagch
minmap = []
minzoruu = sys.maxsize
lastcentroids = []
# anhnii cluster random
centroids = []
for i in clusters:
    # sanamsarguigeer centroid songov
    centroids.append(X[random.randint(0, len(X)-1)])
# print(centroids)
# print(centroids[0][0])
# convergence
# for j in range(k):
done = True
while done:
    map = []
    # print(centroids)
    # buh tseguudiin davtalt
    for dots in X:
        distance = []
        # centroid buriin davtalt
        for centroid in centroids:
            # manhattan distance-iig olov
            dist = getDistance(dots[0], centroid[0], centroid[1], dots[1])
            distance.append(dist)
            # print(dist)
        # hamgiin oiriin centroid iig songov
        minDistance = min(distance)
        # tuhain centroid-iin clusters dah toog map-d hiiv
        map.append(distance.index(minDistance))
        # # hamgiin suuliin index baival
        # if dots == X[-1]:
    newCentroid = [[0,0],[0,0]]
    first = True
    # centroid shinechleh
    for cluster in clusters:
        # print(map)
        sumX = 0
        sumY = 0
        # huuchin centroid oor olson mapaas indexuudiig avav
        clusInd = where(map == cluster)
        # print(clusInd[0])
        # centroid shinechlegdehed ashiglagdah clusterd hamaarah vectoriin niilber
        for i in clusInd[0]:
            sumX += X[i][0]
            # print(i)
            # print(X[i][0])
            sumY += X[i][1]
        # print(sumX)
        # print(len(clusInd[0]))
        # print(len(list(clusInd)))
        # tuhain medianuudiig shine centroid bolgov
        newCentroid[cluster][0] = sumX / len(clusInd[0])
        newCentroid[cluster][1] = sumY / len(clusInd[0])
            # print(newCentroid[1][0])
    count = 0
    # print(len(newCentroid))
    # print(newCentroid)
    # exit()
    for i in range(len(newCentroid)):
        for j in range(len(newCentroid)):
            # print(round(newCentroid[i][j], 2))
            if round(newCentroid[i][j], 4) == round(centroids[i][j], 4):
                count += 1
    if count == 4:
        done = False
    else: 
        centroids = newCentroid
        print(f"centroids: {centroids}")
        # print(f"new centroids: {newCentroid}")
            
        # print(f"clusind = {clusInd}")
    # centroids = []
    
print(f"Centroids: {centroids}")
# print(minmap)
# print(minzoruu)
for cluster in clusters:
    row_ix = where(map == cluster)
    # print(minmap)
    # print(row_ix)
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
pyplot.show()