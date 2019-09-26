import os

# first, open the file
f = open(os.path.join('TestData','MultiLineData.txt'), 'r')
# initializing lists
trial = []
onsetTime = []
respTime = []
# reading one line at a time, then processing
line = f.readline()
while line:
    inString = line.strip().split()
    inNumber = [int(i) for i in inString]
    trial.append(inNumber[0])
    onsetTime.append(inNumber[1])
    respTime.append(inNumber[2])
    # read the next line
    line = f.readline()
    
# always close the file you opened
f.close()

