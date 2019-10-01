import numpy as np

a = np.arange(10)

for i in a:
    print(i)

b = np.arange(15).reshape(5,3)

for row in b:
    print(row)

for row in b:
    for element in row:
        print(element)

for element in b.flat:
    print(element)

