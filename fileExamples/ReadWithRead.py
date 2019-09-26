import os

# first, open the file
f = open(os.path.join('TestData','MultiLineData.txt'), 'r')
# read the entire file content into a string variable fileData
fileData = f.read()
# always close the file you opened
f.close()
