import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
meanCong = np.array([33, 44, 52, 48])
sdCong = np.array([8, 9.1, 10.1, 8.8])
meanIncong = np.array([28, 48, 51.3, 46.5])
sdIncong = np.array([7.2, 9.2, 9.6, 8.4])
meanMixed = np.array([31.3, 40.8, 47.8, 47.2])
sdMixed = np.array([7.8, 8.3, 9.1, 7.8])


# paramters
bar_width = 0.2
x = np.arange(len(meanCong))

# plotting bars
plt.bar(x, meanCong, bar_width)
plt.bar(x+bar_width, meanIncong, bar_width)
plt.bar(x+2*bar_width, meanMixed, bar_width)

# formatting and labeling the axes and title
plt.xlabel('Task')
plt.ylabel('Scores')
plt.title('Scores by tasks')

# and we are done!
plt.show()
