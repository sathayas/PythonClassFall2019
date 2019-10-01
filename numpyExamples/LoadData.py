import numpy as np

infile = np.load('ArrayData.npz')

subjID = infile['subjID']
RT = infile['RT']
score = infile['score']
