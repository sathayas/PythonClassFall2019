import matplotlib.pyplot as plt
import numpy as np

# Generating simple data
t = np.linspace(0,4*np.math.pi,64)
y = np.sin(t)
z = np.cos(t)
w = np.tan(t)

# first, starting a figure
plt.figure(figsize=[6,6])

# first subplot
plt.subplot(221)
plt.plot(t, y, 'b-')
plt.title('Sine function')
plt.ylabel('sin(t)')
plt.xlabel('Angle t (radian)')
plt.axis([0,13,-1.1,1.1])

# second subplot
plt.subplot(222)
plt.plot(t, z, 'b-')
plt.title('Cosine function')
plt.ylabel('cos(t)')
plt.xlabel('Angle t (radian)')
plt.axis([0,13,-1.1,1.1])

# third subplot
plt.subplot(223)
plt.plot(t, w, 'b-')
plt.title('Tangent function')
plt.ylabel('tan(t)')
plt.xlabel('Angle t (radian)')
plt.axis([0,13,-1.1,1.1])

# saving the plot
plt.savefig('Subplots.png')
plt.show()
