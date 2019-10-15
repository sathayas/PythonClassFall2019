import numpy as np

# generating an array of gaussian random number
x = np.random.randn(1000,20)

# calculating meand and sd
x_mean = x.mean(axis=0)
x_sd = x.std(axis=0)

# checking the calculation results
print(x_mean)
print(x_sd)
