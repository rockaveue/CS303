# k-means ангилал
from numpy import unique
from numpy import where
from sklearn.datasets import make_classification
from sklearn.cluster import KMeans
from matplotlib import pyplot
# Датасетыг тодорхойлох
X, _ = make_classification(n_samples=1000, n_features=2,
n_informative=2, n_redundant=0, n_clusters_per_class=1,
random_state=4)
# Моделыг тодорхойлох
model = KMeans(n_clusters=2)
# Моделд тохируулах
model.fit(X)
# Жишээ бүрт кластерыг оноох
yhat = model.predict(X)
# centroids  = model.cluster_centers_
# print(centroids)
# Ялгаатай кластеруудыг хайх
clusters = unique(yhat)
# print(yhat)
print(list(yhat).count(1) - list(yhat).count(0))
# Кластер бүрийн дээжүүдээр сарнилтын график үүсгэх
# print(type(clusters))
for cluster in clusters:
    # Тухайн кластерын дээжийн эгнээний индексийг авах
    row_ix = where(yhat == cluster)
    # print(cluster)
    # print(row_ix)
    # Дээжүүдээр сарнилтын график зурах
    pyplot.scatter(X[row_ix, 0], X[row_ix, 1])
    # print(X[row_ix, 0], X[row_ix, 1])
# # Графикийг харуулах
pyplot.show()