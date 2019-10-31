import numpy as np
import pandas as pd

# experiment data: Scores from
#    control condition:  control
#    condition A:        condA
#    condition B:        condB
#    condition C:        condC
control = np.array([106,  96,  79, 110,  87,  81,  83,  68,  79,  57])
condA = np.array([80, 70, 63, 73, 64, 78, 68, 45, 66, 56])
condB = np.array([ 78,  97, 120,  92,  84, 116,  81,  81, 104,  82])
condC = np.array([ 75,  49,  58, 115,  97,  95,  93,  66,  84,  67])

# Creating an empty dataframe
expData = pd.DataFrame()

# adding variable control under the dataframe, whose values are array control
expData['control'] = control

# adding other variables as well
expData['condA'] = condA
expData['condB'] = condB
expData['condC'] = condC
