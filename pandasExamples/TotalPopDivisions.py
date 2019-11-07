import numpy as np
import pandas as pd

# loading the county-level census data
ctyData = pd.read_csv('co-est2016-alldata.csv',
                      encoding = 'iso-8859-1')

# getting rid of rows with COUNTY==0
ctyData = ctyData[ctyData["COUNTY"]!=0]

# grouping the data by divisions
divData = ctyData.groupby('DIVISION')

# focusing on the 2010 census data (CENSUS2010POP)
print(divData.sum().CENSUS2010POP)

# sorted by divisions
print(divData.sum().sort_values(by='CENSUS2010POP',
                            ascending=False).CENSUS2010POP)
