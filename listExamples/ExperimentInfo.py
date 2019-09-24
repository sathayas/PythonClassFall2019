expCode = [0, 1, 0, 2, 3, 2, 3, 1, 0, 1]
paraCode = ['congruent', 'incongruent', 'mixed', 'null']

# initializing an empty list
fullDesc = []
for iCode in expCode:  # going over each item in the expCode list
    fullDesc = fullDesc + [paraCode[iCode]]   # adding an item -- paradignm name

# printing out the numeric codes as well as the corresponding paradigms
print('Code\tParadigm')
for i,iCode in enumerate(expCode):
    print(iCode, fullDesc[i], sep='\t')
