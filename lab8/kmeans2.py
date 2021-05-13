# k-means ангилал
from numpy import unique
from numpy import where
import numpy as np
from sklearn.datasets import make_classification
from matplotlib import pyplot
import random
import sys
# Датасетыг тодорхойлох
X, _ = make_classification(n_samples=1000, n_features=2,
n_informative=2, n_redundant=0, n_clusters_per_class=1,
random_state=4)
# print(X)
x = []
y = []
print(len(X))
# X deh datag x, y-t huvaaj hiiv
for i in range(len(X)):
    x.append(round(X[i][0], 4))
    y.append(round(X[i][1], 4))
    # print(i)
# X-iin data-g 1 hemjeest massiv bolgov
# dots = X.flatten()
# print(dots)
clusters = [0, 1]
k = 10
print(f"k: {k}")
print(f"clusters: {clusters}")
# yhat baih huvisagch
minmap = []
minzoruu = sys.maxsize
lastcentroids = []
for j in range(k):
    centroids = []
    map = []
    for i in clusters:
        # sanamsarguigeer centroid songov
        centroids.append(X[random.randint(0, len(X)-1)])
    # print(centroids)
    # buh tseguudiin davtalt
    for dots in X:
        # tuhain tsegiin zainuud hadgalah list
        distance = []
        # centroid buriin davtalt
        for centroid in centroids:
            # manhattan distance-iig olov
            dist = abs(dots[0]-centroid[0]) + abs(centroid[1]-dots[1])
            distance.append(dist)
            # print(dist)
        # hamgiin oiriin centroid iig songov
        minDistance = min(distance)
        # tuhain centroid-iin clusters dah toog map-d hiiv
        map.append(distance.index(minDistance))
        # # hamgiin suuliin index baival
        # if dots == X[-1]:
    # map dah 0 bolon 1-n tooniih ni ylgavar
    zoruu = abs(map.count(0) - map.count(1))
    if minzoruu > zoruu:
        minzoruu = zoruu
        minmap = map
        lastcentroids = centroids
print(f"Centroids: {lastcentroids}")
# print(minmap)
print(f"minimum zoruu: {minzoruu}")
clusters = unique(minmap)
for cluster in clusters:
    row_ix = where(minmap == cluster)
    # print(minmap)
    # print(row_ix)
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
pyplot.show()
#----------------------------------------------------------------------
# Моделыг тодорхойлох
# model = KMeans(n_clusters=2)
# Моделд тохируулах
# model.fit(X)
# # Жишээ бүрт кластерыг оноох
# yhat = model.predict(X)
# # Ялгаатай кластеруудыг хайх
# n = 1000
# clusters = unique(yhat)
# # Кластер бүрийн дээжүүдээр сарнилтын график үүсгэх
# clusters = [0, 1]
# for cluster in clusters:
#     # Тухайн кластерын дээжийн эгнээний индексийг авах
#     # row_ix = where(yhat == cluster)
#     # Дээжүүдээр сарнилтын график зурах
#     # pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
#     pyplot.scatter(x, y)
# # Графикийг харуулах
# pyplot.show()