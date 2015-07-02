import numpy as np
import matplotlib, sklearn
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import datasets

iris = datasets.load_iris()
X = iris.data
Y = iris.target


print X[0]
print X[1]

print Y[0]
pca = sklearn.decomposition.PCA(n_components = 2)
pca.fit(X)
X_pca= pca.transform(X)

print X_pca.shape
