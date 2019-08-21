age = 19
hand = 'left'
if (age<20) & (hand=='right'):
    print('Meeting all the requirements.')
else:
    if age<20:
           print('Age requirement is met')
    else:
        print('None of the requirements is met')



# With if...elif...else statement
age = 19
hand = 'left'
if (age<20) & (hand=='right'):
    print('Meeting all the requirements.')
elif age<20:
    print('Age requirement is met')
else:
    print('None of the requirements is met')
