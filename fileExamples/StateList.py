import os

# first, open the file
f = open(os.path.join('TestData','StateList.txt'), 'r')
# read a line, then put in a variable called line
line = f.readline()
# always close the file you opened
f.close()


# converting the line into a list of states
states = line.strip().split(',')

# printing out states
for iState in states:
    print(iState)
