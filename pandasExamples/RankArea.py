import numpy as np
import pandas as pd

# Loading the data
infile = np.load('CryotherapyData.npz') # load the file object
cryoData = pd.DataFrame()  # empty dataframe
for iArray in list(infile.keys()):  # for loop for each array in infile
    cryoData[iArray] = infile[iArray]  # creating a variable for each array

# sorting the dataframe, descending order of area
cryoData.sort_values(by='area', ascending=False, inplace=True)

# adding the rankArea column
cryoData['rankArea'] = np.arange(1,91)


