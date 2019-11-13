import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.decomposition import PCA


# loadin the data
pTraitData = pd.read_csv('personality0.txt', sep=' ')
featureNames = pTraitData.columns  # list of features
