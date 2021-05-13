from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity, cosine_distances, manhattan_distances
from scipy.spatial import distance
import numpy as np
import math
def recursive_check(mylist):
    for i in mylist:
        if type(i) is list:
            yield (i)
            yield from recursive_check(i)
        # else:
        #     yield (i)
def main():
    # X = [[0, 1]]
    # Y = [[2, 0]]
    # X = [[0, 1], [3,5]]
    # Y = [[2, 0], [5,7]]
    lists = []
    X = [[2,4,6, 5 ,6 ], [1,2,4, 2,1], [1,2,5,1,2], [0, 2, 6,2,3]]
    Y = [[2,5,6, 1, 2], [1,6,14,6,5], [10,2,0,4,2], [0, 2, 1,7,8]]
    # X = [[10, 1, 2, 0], [0, 1, 2, 0], [0, 1, 2, 1]]
    # Y = [[4, 1, 2, 1], [5, 1, 2, 5], [1, 1, 2, 1]]
    # for i in recursive_check(X):
    #     if len(list(recursive_check(X))):
            # print(f"x[{i}] = {list(recursive_check(X))[i]}, y[{j}] = {list(recursive_check(Y))[j]}\n")
            
    # euclid
    # sqrt(summai((xi-yi)^2))
    euclid = []
    for i in range(len(X)):
        el = []
        for j in range(len(Y)):
            zip_object = zip(X[i], Y[j])
            b = 0
            for list1, list2 in zip_object:
                b += pow(list1-list2 , 2) 
                # el.append(b)
            el.append(math.sqrt(b))
            # print(el)
        euclid.append(el)
        # lists.append(i)
    # for list1, list2, list3 in lists:
    #     difference.append(pow((list1 - list2), 2))
    # print(recursive_check(X))
    print ("euclid: хийсэн")
    for i in euclid:
        print(i)
    # print(euclid)
    # X = [[1]]
    # Y = [[9]]
    # dst = distance.euclidean(X,Y)
    # print('Евклидийн алслал нь: %.3f' % dst)
    print(f'euclid: бэлэн сан\n{euclidean_distances(X, Y)}')
    # ------------------------------------------------------------------
    # Manhattan
    # summai(module(xi-yi))
    manhattan = []
    for i in range(len(X)):
        el = []
        for j in range(len(X)):
            zip_object = zip(X[i], Y[j])
            # print(f"x[{i}] = {list(recursive_check(X))[i]}, y[{j}] = {list(recursive_check(Y))[j]}\n")
            b = 0
            for list1, list2 in zip_object:
                b += abs(list1-list2 )
                # el.append(b)
            el.append(b)
            # print(el)
        manhattan.append(el)
    print("manhattan: хийсэн")
    for i in manhattan:
        print(i)
    # dst1 = distance.cityblock(X,Y)
    # print('Манхаттан алслал: %.3f' % dst1)
    print(f'Манхаттан алслал: бэлэн сан\n {manhattan_distances(X, Y)}')
    # -------------------------------------------------------------------
    # cosine
    # (summai(xiyi))/(sqrt(summai( xi^2))*sqrt(summai(yi^2)))
    
    
    # X = [[10, 1, 2, 0], [0, 1, 2, 0], [0, 1, 2, 1]]
    # Y = [[4, 1, 2, 1], [5, 1, 2, 5], [1, 1, 2, 1]]
    cosine = []
    for i in range(len(X)):
        el = []
        for j in range(len(X)):
            zip_object = zip(X[i], Y[j])
            # print(f"x[{i}] = {list(recursive_check(X))[i]}, y[{j}] = {list(recursive_check(Y))[j]}\n")
            b = 0
            c = 0
            d = 0
            for list1, list2 in zip_object:
                b += list1*list2
                c += pow(list1, 2)
                d += pow(list2, 2)
                # print (f"b = {b}, c = {c}, d = {d} \n")
                # el.append(b)
            el.append((b / (math.sqrt(c) * math.sqrt(d))))
            # print(f"el = {el}")
        cosine.append(el)
    print("cosine: хийсэн")
    for i in cosine:
        print(i)
    
    cos_sim = cosine_similarity(X, Y)
    # print(f'Косайн зайн нь: \n{cosine_distances(X,Y)}' )
    print(f'Косайн зай: бэлэн сан\n{cos_sim}')
    # K Means
    # summaj(summai(module(xi^j-cj)^2))
    # n ni ith cluster dah ugugdliin tseguudiin too
    # k ni cluster tuvuudiin too

if __name__ == '__main__':
    main()