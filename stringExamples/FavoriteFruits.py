# case sensitive version (original)
print('What is your favorite fruit?')
userFruit = input()

if userFruit == 'apple':
    print('I like ' + userFruit + ' too.')
else:
    print('I eat ' + userFruit + ' occasionally')


# converting the input to lower case
print('What is your favorite fruit?')
userFruit = input().lower()

if userFruit == 'apple':
    print('I like ' + userFruit + ' too.')
else:
    print('I eat ' + userFruit + ' occasionally')
