import numpy as np
import pandas as pd

expData = pd.read_csv('ExpData.csv',index_col=0)

# simple descriptive stats
expData.mean()
expData.std()
expData.median()

# correlation
expData.corr()

# ranking
expData.rank()
expData.control.rank()
