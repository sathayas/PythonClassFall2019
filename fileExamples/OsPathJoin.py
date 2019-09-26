# import the os module
import os

# Home directory
homeDir = 'Some_home_directory'
# Directories for subjects 
subjects = ['sub001', 'sub003', 'sub005']
# Experiment outcome data files
expData = ['congruent.txt', 'incongruent.txt', 'mixed.txt']

for iSubj in subjects:
    for iExp in expData:
        dataFullPath = os.path.join(homeDir, iSubj, iExp)
        print(dataFullPath)


