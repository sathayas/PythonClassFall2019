userStr = input('Please enter your last name or UTEID: ')
if userStr.isalpha():
    print('Your last name is ' + userStr.upper())
elif userStr.isalnum():
    print('Your UT EID is ' + userStr.lower())
