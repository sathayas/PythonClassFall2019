import matplotlib.pyplot as plt
x = list(range(13))
plt.plot(x,[y**2 for y in x])
plt.title('Some plot')
plt.show()
