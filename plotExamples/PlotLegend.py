import matplotlib.pyplot as plt
import numpy as np

# Generating simple data
t = np.linspace(0,4*np.math.pi,64)
y = np.sin(t)

# plotting the data with labels
plt.plot(t, y, 'b-', label='Blue curve')
plt.plot(t, y+0.2, 'g.', label='Green dots')
plt.plot(t, y+0.4, 'ro', label='Red circles')
# and creating a legend
plt.legend(loc=1)
plt.show()

