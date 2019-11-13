import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# loadin the data
pTraitData = pd.read_csv('personality0.txt', sep=' ')
numFeatures = len(pTraitData.columns)  # number of features



# determinging the number of clusters (up to 30 clusters)
SSE = []
nMaxClusters = 30
for iClus in range(1,nMaxClusters+1):
    # K-means clustering
    km = KMeans(n_clusters=iClus)  # K-means with a given number of clusters
    km.fit(pTraitData)  # fitting the personality data
    SSE.append(km.inertia_) # recording the sum of square distances

# plotting the sum of square distance
plt.plot(np.arange(1,nMaxClusters+1),SSE,marker = "o")
plt.xlabel('Number of clusters')
plt.ylabel('Sum of sq distances')
plt.show()
