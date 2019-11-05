import numpy as np
import pandas as pd

# Version 1
# loading arrays from the .npz file
infile = np.load('CryotherapyData.npz') # load the file object
age = infile['age']
time = infile['time']
area = infile['area']
success = infile['success']

# creaging a dataframe with these arrays
cryoData = pd.DataFrame()
cryoData['age'] = age
cryoData['time'] = time
cryoData['area'] = area
cryoData['success'] = success



# Version 2
# Or, using keys from infile
infile = np.load('CryotherapyData.npz') # load the file object
cryoData = pd.DataFrame()  # empty dataframe
for iArray in list(infile.keys()):  # for loop for each array in infile
    cryoData[iArray] = infile[iArray]  # creating a variable for each array
    
