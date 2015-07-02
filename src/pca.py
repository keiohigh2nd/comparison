import numpy as np
import matplotlib, sklearn
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA
from sklearn import datasets

pca = sklearn.decomposition.PCA(n_components = 2)

pca.fit(datasets.getData())
transformed = pca.transform(dataset.getData())
colors = [plt.cm.hsv(0.1*i, 1) for i in range(10)]
plt.figure(figsize=(16,11))
for i in range(10):
    plt.scatter(0,0, alpha=1, c=colors[i],label=str(i))
plt.legend()

for l, d in zip(dataset.getLabel(), transformed):
    plt.scatter(d[0],d[1] , c=colors[int(l)], alpha=0.3)

plt.title("PCA(Principal Component Analysis)")
plt.show()

transformed = [pca.transform(dataset.getByLabel(label=i,num=('all'))) for i in range(10)]

ave = [np.average(transformed[i],axis=0) for i in range(10)]
var = [np.var(transformed[i],axis=0) for i in range(10)]
plt.clf()
plt.figure(figsize=(14,10))
for j in range(10):
    plt.scatter(100,100, alpha=1, c=colors[j],label=str(j))
plt.legend()
plt.xlim(-1500, 1500)
plt.ylim(-1500, 1500)

for i, a, v in zip(range(10), ave, var):
    print i, a[0], a[1]
    plt.scatter(a[0], a[1], c=colors[i], alpha=0.6, s=v/4, linewidth=1)
    plt.scatter(a[0], a[1], c="k", s=10)    
    plt.text(a[0], a[1], "digit: %d"%i, fontsize=12)

plt.title("PCA Representative Vector for each digit.")
plt.savefig("PCA_RepVec.png")
plt.show()


"""
iris = datasets.load_iris()
X = iris.data
Y = iris.target

X.shape

pca = sklearn.decomposition.PCA(n_components = 2)
pca.fit(X)
X_pca= pca.transform(X)

print X_pca.shape
"""

