import numpy as np
import pandas as pd

# loading the county-level census data
ctyData = pd.read_csv('co-est2016-alldata.csv',
                      encoding = 'iso-8859-1')

# getting rid of rows with COUNTY==0
ctyData = ctyData[ctyData["COUNTY"]!=0]

# grouping the data by states
stateData = ctyData.groupby('STNAME')

# information grouped by states
stateData.size()
stateData.mean()

# focusing on the 2010 census data (CENSUS2010POP)
stateData.sum().CENSUS2010POP
stateData.sum().sort_values(by='CENSUS2010POP',
                            ascending=False).CENSUS2010POP.head(10)


# grouping by the divisions and states
divStateData = ctyData.groupby(['DIVISION','STNAME'])

# checking the resulting grouping
divStateData.size()
divStateData.sum().CENSUS2010POP
