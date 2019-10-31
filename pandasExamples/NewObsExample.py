import numpy as np
import pandas as pd

expData = pd.read_csv('ExpData.csv', index_col=0)

# a new observation to be added
newObs = [55, 88, 86, 70]
expData.loc[len(expData)] = newObs

