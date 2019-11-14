import numpy as np
import pandas as pd
from sklearn.cluster import KMeans
from sklearn.metrics import adjusted_rand_score, adjusted_mutual_info_score

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

# K-means clustering
numClus = 3  # number of clusters
km = KMeans(n_clusters=numClus)  # defining the clustering object
km.fit(seedFeatures)  # actually fitting the data
y_clus = km.labels_   # clustering info resulting from K-means


# ARI  &  AMI
print('ARI =  %7.4f' % adjusted_rand_score(seedTargets, y_clus))
print('AMI =  %7.4f' % adjusted_mutual_info_score(seedTargets, y_clus))
