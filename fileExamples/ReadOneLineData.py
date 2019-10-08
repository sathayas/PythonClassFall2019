import os

# first, open the file
f = open(os.path.join('TestData','ExerciseData_OneLine.txt'), 'r')
# read a line, then put in a variable called line
line = f.readline()
# always close the file you opened
f.close()


# converting strings to numbers
inString = line.strip().split()
inNumber = [int(i) for i in inString]


# putting them into approriate lists
trial = inNumber[:3]
onsetTime = inNumber[3:6]
respTime = inNumber[6:9]
score = inNumber[9:]

# Checking the lists
print(trial)
print(onsetTime)
print(respTime)
print(score)
