import matplotlib.pyplot as plt
import numpy as np

# Generating simple data
t = np.linspace(0,4*np.math.pi,64)
y = np.sin(t)

# plotting the data
plt.plot(t, y, 'b-')
plt.plot(t, y+0.2, 'g.')
plt.plot(t, y+0.4, 'ro')
plt.plot(t, y+0.6, 'cs')
plt.plot(t, y+0.8, 'm^')
plt.plot(t, y+1.0, 'yx')
plt.plot(t, y+1.2, 'kD')
plt.show()


# plotting the data
plt.plot(t, y, 'k-')
plt.plot(t, y, 'rs')
plt.show()
