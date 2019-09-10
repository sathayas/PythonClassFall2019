trueNumber = 10
userNumber = int(input('Guess the number (1-20): '))

while userNumber !=trueNumber:
    if userNumber > trueNumber:
        print('Too high')
    else:
        print('Too low')
    userNumber = int(input('Guess the number (1-20): '))

print('You guessed it!')
