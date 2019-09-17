# a sample dictionary
respTime = {'congruent':132, 'incongruent':250, 'mixed':189}

# for loop over keys
for iKey in respTime.keys():
    print('Condition: ' + iKey)

# for loop over items
print('Repsponse times:')
for iKey, iValue in respTime.items():
    print(str(iValue) + ' (' + iKey + ')')
