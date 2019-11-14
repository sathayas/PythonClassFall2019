import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# loadin the data
pTraitData = pd.read_csv('personality0.txt', sep=' ')
featureNames = pTraitData.columns  # list of features


# determinging the number of clusters (up to 30 clusters)
#
#  EXERCISE: GENERATE A SCREE PLOT AND DETERMINE THE NUMBER OF CLUSTERS
#
#

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
