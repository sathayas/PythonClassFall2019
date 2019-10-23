import matplotlib.pyplot as plt
import numpy as np

# Generating simple data
t = np.linspace(0,4*np.math.pi,64)
y = np.sin(t)

# The range of the axes are controlled now
plt.plot(t, y, 'b-')
plt.title('Sine function')
plt.ylabel('sin(t)')
plt.xlabel('Angle t (radian)')
plt.axis([0,13,-2,2])
plt.savefig('SinPlot.png', dpi=300)
plt.show()
