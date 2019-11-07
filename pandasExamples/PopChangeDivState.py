import numpy as np
import pandas as pd

# loading the county-level census data
ctyData = pd.read_csv('co-est2016-alldata.csv',
                      encoding = 'iso-8859-1')

# getting rid of rows with COUNTY==0
ctyData = ctyData[ctyData["COUNTY"]!=0]

# grouping by the divisions and states
divStateData = ctyData.groupby(['DIVISION','STNAME'])

# population change, then printing out by division and by state
print(divStateData.NPOPCHG_2016.sum())
