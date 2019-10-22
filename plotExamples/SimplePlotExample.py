import matplotlib.pyplot as plt
import numpy as np

# Generating simple data
t = np.linspace(0,4*np.math.pi,64)
y = np.sin(t)

# plotting the data
plt.plot(t, y)
plt.show()
