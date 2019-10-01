import numpy as np

subjID = np.array(['sub001']*3 + ['sub005']*4 + ['sub010']*3)
RT = np.array([ 98,  96,  86,  90,  95,  80, 117,  90, 114, 113])
score = np.array([0, 0, 1, 0, 1, 0, 0, 0, 1, 0])

np.savez('ArrayData.npz', subjID=subjID, RT=RT, score=score)
