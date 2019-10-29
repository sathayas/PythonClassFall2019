import matplotlib.pyplot as plt
import numpy as np

cond = np.array([1, 1, 1, 1, 1, 2, 2, 2, 2, 2, 3, 3, 3, 3, 3, 3])
x = np.array([ 20, 40, 60, 80, 100, 20, 40, 60, 80, 100, 20, 40,
               60, 80, 100, 120])
y = np.array([109, 98, 121, 88, 109, 115, 133, 117, 122, 131,
              133, 163, 153, 131, 159, 144])

plt.plot(x[cond==1], y[cond==1], 'b-')
plt.plot(x[cond==2], y[cond==2], 'm-')
plt.plot(x[cond==3], y[cond==3], 'k-')

plt.title('Response time by condition')
plt.xlabel('Onset time (s)')
plt.ylabel('Response time (ms)')
plt.axis([10, 130, 85, 175])

plt.show()
