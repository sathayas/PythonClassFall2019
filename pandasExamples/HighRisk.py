import numpy as np
import pandas as pd

# Loading the data
infile = np.load('CryotherapyData.npz') # load the file object
cryoData = pd.DataFrame()  # empty dataframe
for iArray in list(infile.keys()):  # for loop for each array in infile
    cryoData[iArray] = infile[iArray]  # creating a variable for each array

# success rate for the high risk group
p_HighRisk = cryoData[(cryoData.age>=30) & (cryoData.time>=8)].success.mean()
print('Success rate for the high-risk group: %5.3f' % p_HighRisk)

# success rate for all
p_All = cryoData.success.mean()
print('Success rate for all: %5.3f' % p_All)


