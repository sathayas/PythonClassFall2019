import random

# function to roll two dice and return
def rollDice():
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
    return dice1, dice2

# rolling until you get snake eyes
while True:
    d1, d2 = rollDice()
    print('Dice 1: ' + str(d1) + '   Dice 2: ' + str(d2))
    if d1==1 and d2==1:
        break
print('You rolled snake eyes!')
