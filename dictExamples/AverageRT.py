respTime = {'congruent':132, 'incongruent':250, 'mixed':189}

sumRT = 0
for iKey, iValue in respTime.items():
    sumRT += iValue  # equvalent to sumRT = sumRT + iValue

avgRT = sumRT/len(respTime)  # calculating the average RT
respTime['average'] = avgRT  # adding the new item to the dictionary

# printing out the updated dictionary
print(respTime)
