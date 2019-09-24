#mammal = ['cat', 'dog', 'cat', 'cat', 'tiger']
mammal = ['cat', 'dog', 'cat', 'cat', 'tiger',
          'bear', 'panda', 'cat', 'cat', 'gorilla',
          'cat', 'armadillo']

while 'cat' in mammal:
    mammal[mammal.index('cat')] = 'lion'

print(mammal)
