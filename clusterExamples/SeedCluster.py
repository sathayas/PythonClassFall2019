import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

# loadin the data
seedData = pd.read_csv('seeds_dataset.txt', sep='\t', header=None)
seedFeatures = np.array(seedData.iloc[:,:7])
seedTargets = np.array(seedData.iloc[:,7])
targetNames = ['Kama','Rosa','Canadian']
targetColors = ['red','blue','green']

#
#
# Code for exercise. Determine 7 PCs in an array named seedPCs
#
#

# plotting the first 2 PCs
for iTarget in np.arange(1,4):
    plt.plot(seedPCs[seedTargets==iTarget,0],
             seedPCs[seedTargets==iTarget,1],
             marker='.', ls='none',
             c=targetColors[iTarget-1], label=targetNames[iTarget-1])
plt.xlabel('PC1')
plt.ylabel('PC2')
plt.legend(loc=4)
plt.show()
