import os

# first, open the file
f = open(os.path.join('TestData','StateCapitalList.txt'), 'r')
# read all the lines, then put in a list called stateList
stateList = f.readlines()
# always close the file you opened
f.close()

# printing out, one state at a time
for iState in stateList:
    state, capital = iState.strip().split(',')
    print(capital + ' (' + state + ')')
