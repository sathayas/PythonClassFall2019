import numpy as np
import matplotlib.pyplot as plt

meanData = np.array([20, 35, 30, 35, 27])
stdData = np.array([2, 3, 4, 1, 2])
x = np.arange(1,6)

# just plotting bars
plt.bar(x, meanData)
plt.show()

# bar width and colors
plt.bar(x, meanData, 0.4, color='m')
plt.show()

# error bars added
plt.bar(x, meanData, 0.4, yerr=stdData, color='m')
plt.show()

# formatting the x- and y-axis, adding the title
plt.bar(x, meanData, 0.4, yerr=stdData, color='m')
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by groups')
plt.xticks(x+0.2, ['1', '2', '3', '4', '5'])
plt.show()


