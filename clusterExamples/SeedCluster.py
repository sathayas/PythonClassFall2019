import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

# loadin the data
seedData = pd.read_csv('seeds_dataset.txt', sep='\t', header=None)
seedFeatures = np.array(seedData.iloc[:,:7])
seedTargets = np.array(seedData.iloc[:,7])
targetNames = ['Kama','Rosa','Canadian']

# feature names
featureNames = ['area',
                'perimeter',
                'compactness',
                'length of kernel',
                'width of kernel',
                'asymmetry coefficient',
                'length of kernel groove',
                'class']
seedData.columns = featureNames


# creating a list of colors
yColor = []
colorVector = 'rgb'
for iClass in range(1,4):
    yColor = yColor + ([colorVector[iClass-1]] * len(seedTargets[seedTargets==iClass]))

# plotting the scatter plot matrix
pd.plotting.scatter_matrix(seedData.iloc[:,:7], figsize=[9,9], color=yColor)
plt.show()



# K-means clustering
#
# EXERCISE: FILL IN THE CODE TO PERFORM K-MEANS CLUSTERING
#


### plotting the clusters
plt.figure(figsize=[8,4])
xFeature = 6
yFeature = 5
# First, results from K-means
plt.subplot(121)
plt.scatter(seedFeatures[:,xFeature],
            seedFeatures[:,yFeature], c=y_clus, marker='+')
plt.xlabel(featureNames[xFeature])
plt.ylabel(featureNames[yFeature])
plt.title('Clusters from K-means')

# As a comparison, the true clusters
plt.subplot(122)
plt.scatter(seedFeatures[:,xFeature],
            seedFeatures[:,yFeature], c=yColor, marker='+')
plt.xlabel(featureNames[xFeature])
plt.ylabel(featureNames[yFeature])
plt.title('True clusters')

plt.show()
