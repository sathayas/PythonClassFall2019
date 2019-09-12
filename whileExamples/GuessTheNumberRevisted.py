trueNumber = 10
while True:
    userNumber = int(input('Guess the number (1-20): '))
    if userNumber == trueNumber:
        break
    elif userNumber > trueNumber:
        print('Too high')
    else:
        print('Too low')

print('You guessed it!')
