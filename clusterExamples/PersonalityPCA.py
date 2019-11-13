import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# loadin the data
pTraitData = pd.read_csv('personality0.txt', sep=' ')
featureNames = pTraitData.columns  # list of features


# K-means clustering with 3 clusters
nClus = 3
km = KMeans(n_clusters=nClus)
km.fit(pTraitData)  # fitting the principal components
y_clus = km.labels_   # clustering info resulting from K-means


# transforming the original features to 2-dimensional space
# applying PCA
pca = PCA(n_components=2)  # creating a PCA transformation with 2 PCs
PC = pca.fit_transform(pTraitData) # fit the data, get 2 PCs



### plotting the clusters
# plotting PCs with clusters indicated
plt.scatter(PC[:,0], PC[:,1],c=y_clus,marker='+')
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.title('Dimension reduced data with clusters')
plt.show()
