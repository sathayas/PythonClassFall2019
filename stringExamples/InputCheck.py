
while True:
    print('Please enter your 5-digit ZIP code')
    yourZIP = input()
    if yourZIP.isdecimal():
        break
    print('A ZIP code can only have numbers')

while True:
    print('Please enter a word')
    yourWord = input()
    if yourWord.isalpha():
        break
    print('That is not a proper word. Try again')

while True:
    print('Choose a new password (letters and numbers only)')
    yourPassword = input()
    if yourPassword.isalnum():
        break
    print('That is not a proper password. Try again')
