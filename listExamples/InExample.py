passwdList = ['abc123', '8875', 'Good!', 'Python3.6']
while True:
    userPasswd = input('What is the password? ')
    if userPasswd in passwdList:
        break
    else:
        print('Invalid password! Try again.')

print('Access granted!')
