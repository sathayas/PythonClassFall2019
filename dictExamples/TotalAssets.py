inventory = {
 'computer': 5,
 'centrifuge': 4,
 'freezer': 1,
 'incubator': 2,
 'microscope': 2
}
unitPrice = {
 'computer': 1800,
 'centrifuge': 2000,
 'freezer': 1300,
 'microscope': 4500,
 'refrigerator': 1800,
 'incubator': 500,
 'scale': 400,
 'spectrometer': 2100
}

# initializing the totalEstValue dictionary
totalEstValue = {}

# loop over itmes in unitPrice dictionary
for iKey,iValue in unitPrice.items():
    totalEstValue[iKey] = iValue * inventory.get(iKey,0)

# checking the dictionary to see if the calculation is correct
print(totalEstValue)
