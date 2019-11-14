import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# loadin the data
pTraitData = pd.read_csv('personality0.txt', sep=' ')
featureNames = pTraitData.columns  # list of features


# determinging the number of clusters (up to 30 clusters)
SSE = []
for iClus in range(1,31):
    # K-means clustering
    km = KMeans(n_clusters=iClus)  # K-means with a given number of clusters
    km.fit(pTraitData)  # fitting the principal components
    SSE.append(km.inertia_) # recording the sum of square distances

# plotting the sum of square distance
plt.plot(np.arange(1,31),SSE,marker = "o")
plt.xlabel('Number of clusters')
plt.ylabel('Sum of sq distances')
plt.show()



# K-means clustering again
# We will go with 3 clusters (btw is not the best solution)
nClus = 3
km = KMeans(n_clusters=nClus)
km.fit(pTraitData)  # fitting the principal components
y_clus = km.labels_   # clustering info resulting from K-means


### plotting the clusters
# with two of the features
xFeature = 21 # index for the feature on the x-axis
yFeature = 28 # index for the feature on the y-axis
plt.scatter(pTraitData.iloc[:,xFeature],
            pTraitData.iloc[:,yFeature],c=y_clus,marker='+')
plt.xlabel(featureNames[xFeature])
plt.ylabel(featureNames[yFeature])
plt.title(featureNames[xFeature] + ' v.s. ' + featureNames[yFeature])
plt.show()
