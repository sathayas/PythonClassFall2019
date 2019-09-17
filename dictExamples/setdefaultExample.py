message = 'the quick brown fox jumps over the lazy dog'
count = {}   # initializing the counter
for iLetter in message:
    count.setdefault(iLetter,0)
    count[iLetter] += 1

print('Frequency counts of letters')
for iKey, iValue in count.items():
    print(iKey + ': ' + str(iValue))

