age = 44
if age<20:
    print('You met the age criterion')
else:
    print('You did not meet the age criterion')



age = 44
hand = 'left'
if (age<20) & (hand=='right'):
    print('The age is ' + str(age) + ' years old.')
    print('The handedness is ' + hand + '-handed.')
    print('Meeting all the requirements.')
else:
    print('Age requirement: younger than 20')
    print('Handedness requirement: right-handed')
    print('You did not meet either requirement')
