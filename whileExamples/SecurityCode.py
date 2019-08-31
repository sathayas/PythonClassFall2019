# the secret security code
securityCode = '8577'
# ask the user to enter a code
userCode = input('Please enter the security code ')

# the while loop
while userCode != securityCode:

    # printing out a message depending on the entered code
    if userCode == '1234' or userCode == '9999':
        print('That is not a secure security code!')
    else:
        print('Invalid security code! Try again.')

    # asking the user to re-enter the code
    userCode = input('Please enter the security code ')
    
# After you figure out the security code
print('Congrats! You entered the correct security code!')

