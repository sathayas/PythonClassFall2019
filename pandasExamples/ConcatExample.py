import numpy as np
import pandas as pd

# Two separate dataframes
expData1 = pd.read_csv('ExpData1.csv')
expData1.drop('Unnamed: 0', axis=1, inplace=True)
expData2 = pd.read_csv('ExpData2.csv')
expData2.drop('Unnamed: 0', axis=1, inplace=True)

# concatenating the two
expDataConcat = pd.concat([expData1, expData2], ignore_index=True)
expDataAppend = expData1.append(expData2, ignore_index=True)


