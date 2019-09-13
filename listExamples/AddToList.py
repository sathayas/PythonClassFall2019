# a function to append a new item to the list
def append_item(origList):
    newList = origList
    newList.append('New item')
    return newList

# original list
aList = ['apple', 'banana', 'cat']
print(aList)

# the new list with a new item
bList = append_item(aList)
print(bList)

# original list again
print(aList)
