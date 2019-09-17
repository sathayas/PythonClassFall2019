numAccident = {'A':5, 'C':2, 'D':1, 'F':2, 'H':1}
totalAccident = 0
for i in 'ABCDEGFHIJK':
    totalAccident = totalAccident + numAccident.get(i,0)

print('Total accidents: ' + str(totalAccident))
