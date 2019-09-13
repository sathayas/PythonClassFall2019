# importing the copy module
import copy

def append_item(origList):
    # make a copy of the original list
    newList = copy.copy(origList)
    # then append the new item to the newly created list
    newList.append('New item')
    return newList

aList = ['apple', 'banana', 'cat']
bList = append_item(aList)
print(aList)
print(bList)

