def noFirstLast(inList):
    outList = inList[1:-1]
    return outList

animals = ['dog', 'cat', 'tiger', 'lion', 'moose', 'panda', 'bear']
print(animals)
print(noFirstLast(animals))

fruits = ['apple', 'orange', 'banana', 'pineapple']
print(fruits)
print(noFirstLast(fruits))

memberNames = ['Paul', 'John', 'George', 'Ringo', 'Yoko']
print(memberNames)
print(noFirstLast(memberNames))
