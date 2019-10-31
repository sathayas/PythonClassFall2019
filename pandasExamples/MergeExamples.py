import numpy as np
import pandas as pd

# reading two dataframes
expDataControl = pd.read_csv('ExpDataControl.csv',index_col=0)
expDataABC = pd.read_csv('ExpDataABC.csv',index_col=0)

# merging the two dataframes, based on the ID
expData = pd.merge(expDataControl, expDataABC, on='ID')

# reading another dataframe
expDataDE = pd.read_csv('ExpDataDE.csv',index_col=0)

# merging the full dataframe with the new dataframe
expDataInner = pd.merge(expData, expDataDE, on='ID')
expDataOuter = pd.merge(expData, expDataDE, on='ID', how='outer')
