from sklearn.metrics.pairwise import euclidean_distances, cosine_similarity, cosine_distances, manhattan_distances
from scipy.spatial import distance
import numpy as np
import math

def main():
    # ashiglaj boloh uur uur ugugdluud
    # X = [[0, 1]]
    # Y = [[2, 0]]
    # X = [[0, 1], [3,5]]
    # Y = [[2, 0], [5,7]]
    X = [[2,4,6, 5 ,6 ], [1,2,4, 2,1], [1,2,5,1,2], [0, 2, 6,2,3]]
    Y = [[2,5,6, 1, 2], [1,6,14,6,5], [10,2,0,4,2], [0, 2, 1,7,8]]
    # X = [[10, 1, 2, 0], [0, 1, 2, 0], [0, 1, 2, 1]]
    # Y = [[4, 1, 2, 1], [5, 1, 2, 5], [1, 1, 2, 1]]
    # euclid
    # sqrt(summai((xi-yi)^2))
    
    euclid = []
    # эхний Х цэгийн тоогоор давтах давталт
    for i in range(len(X)):
        el = []
        # дараагийн Y цэгийн тоогоор давтах давталт
        for j in range(len(Y)):
            # Сонгогдсон 2 цэгийг zip ашиглаж нэг list рүү оруулав
            zip_object = zip(X[i], Y[j])
            # Нийлбэр байх хувьсагч
            b = 0
            # листээ задлаад векторуудын ялгаврын квадратын нийлбэр олох давталт
            for list1, list2 in zip_object:
                b += pow(list1-list2 , 2) 
            # дээр үүссэн нийлбэрийн язгуурыг el хувьсагчид хийв
            el.append(math.sqrt(b))
        # дээр байх давталт дуусангуут Y-ийн тоотой ижил тоотой хувьсагчийг euclid-д хийв
        euclid.append(el)
        
    print ("euclid: хийсэн")
    # euclid хувьсагчийг хэвлэсэн нь
    for i in euclid:
        print(i)
    # Бэлэн сан ашиглаж гаргасан нь
    print(f'euclid: бэлэн сан\n{euclidean_distances(X, Y)}')
    # ---------------------------------------------------------------------------------
    # Manhattan
    # summai(module(xi-yi))
    manhattan = []
    # эхний Х цэгийн тоогоор давтах давталт
    for i in range(len(X)):
        el = []
        # дараагийн Y цэгийн тоогоор давтах давталт
        for j in range(len(Y)):
            # Сонгогдсон 2 цэгийг zip ашиглаж нэг list рүү оруулав
            zip_object = zip(X[i], Y[j])
            # Нийлбэр байх хувьсагч
            b = 0
            # листээ задлаад векторуудын ялгаврын модулийн нийлбэр олох давталт
            for list1, list2 in zip_object:
                b += abs(list1-list2 )
            # дээр үүссэн нийлбэрийг el хувьсагчид хийв
            el.append(b)
        # дээр байх давталт дуусангуут Y-ийн тоотой ижил тоотой хувьсагчийг manhattan-д хийв
        manhattan.append(el)
        
    print("manhattan: хийсэн")
    # manhattan хувьсагчийг хэвлэсэн нь
    for i in manhattan:
        print(i)
        
    # Бэлэн сан ашиглаж гаргасан нь
    print(f'Манхаттан алслал: бэлэн сан\n {manhattan_distances(X, Y)}')
    # ---------------------------------------------------------------------------------
    # cosine
    # (summai(xiyi))/(sqrt(summai( xi^2))*sqrt(summai(yi^2)))
    
    cosine = []
    # эхний Х цэгийн тоогоор давтах давталт
    for i in range(len(X)):
        el = []
        # дараагийн Y цэгийн тоогоор давтах давталт
        for j in range(len(Y)):
            # Сонгогдсон 2 цэгийг zip ашиглаж нэг list рүү оруулав
            zip_object = zip(X[i], Y[j])
            # Нийлбэр байх хувьсагчид
            b = 0
            c = 0
            d = 0
            # листээ задлаад векторуудын ялгаврын модулийн нийлбэр олох давталт
            for list1, list2 in zip_object:
                b += list1*list2
                c += pow(list1, 2)
                d += pow(list2, 2)
            # дээр үүссэн нийлбэрүүдийг томъёоны дагуу el хувьсагчид хийв
            el.append((b / (math.sqrt(c) * math.sqrt(d))))
        # дээр байх давталт дуусангуут Y-ийн тоотой ижил тоотой хувьсагчийг cosine-д хийв
        cosine.append(el)
        
    print("cosine: хийсэн")
    # cosine хувьсагчийг хэвлэсэн нь
    for i in cosine:
        print(i)
    
    # Бэлэн сан ашиглаж гаргасан нь
    cos_sim = cosine_similarity(X, Y)
    print(f'Косайн зай: бэлэн сан\n{cos_sim}')

if __name__ == '__main__':
    main()