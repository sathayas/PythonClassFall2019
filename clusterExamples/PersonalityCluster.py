import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans


# loadin the data
pTraitData = pd.read_csv('personality0.txt', sep=' ')

numFeatures = 32
