import numpy as np

# data arrays
RTMat = np.array([[111, 100,  86, 120,  91],
                  [ 92,  83, 105, 103, 112],
                  [117, 121, 124, 111, 110],
                  [111,  86, 113,  88, 105]])
scoreMat = np.array([[1, 0, 0, 0, 0],
                     [0, 1, 1, 0, 1],
                     [0, 1, 1, 0, 0],
                     [0, 0, 1, 1, 0]])

# for loop for scores
for iScore in range(2):
    meanRT = RTMat[scoreMat==iScore].mean() # calculating mean
    stdRT = RTMat[scoreMat==iScore].std()   # calculating sd
    print('Score : %d' % iScore + '\t Mean: %5.1f' % meanRT
          + '\t SD: %4.1f' % stdRT)

