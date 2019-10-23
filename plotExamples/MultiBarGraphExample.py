import numpy as np
import matplotlib.pyplot as plt

# data to be plotted
means_men = (20, 35, 30, 35, 27)
std_men = (2, 3, 4, 1, 2)
means_women = (25, 32, 34, 20, 25)
std_women = (3, 5, 2, 3, 3)

# paramters
bar_width = 0.3
x = np.arange(len(means_men))

# plotting bars
plt.bar(x, means_men, bar_width, yerr=std_men,
        color='b', label='Men')
plt.bar(x+bar_width, means_women, bar_width, yerr=std_women,
        color='r', label='Women')

# formatting and labeling the axes and title
plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by groups')

# formatting ticks for the x-axis
plt.xticks(x+bar_width, ['1', '2', '3', '4', '5'])

# adding the legend
plt.legend()

# and we are done!
plt.show()
