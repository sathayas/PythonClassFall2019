nameList = ['Sarah', 'Paul', 'Jill', 'Robert']

while True:
    userName = input('What is your name? ')
    if userName=='End':
        break
    elif userName in nameList:
        print('You are on the list')
    else:
        print('Your name has been added to the list')
        nameList = nameList + [userName]

print('Final name list:')
print(nameList)
