def HandednessAge(hand, age):
    # hand: Handedness, 'left' or 'right'
    # age: Age in years
    print('You are ' + str(age) + ' years old and ' + hand + '-handed.')

HandednessAge('right', 33)
HandednessAge('left',18)
HandednessAge('right')
HandednessAge(18,'left')
HandednessAge(age=18, hand='left')

