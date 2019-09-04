# Printing are we there yet 10 times
for i in range(10):
    print('Are we there yet?')


# printing i inside a for loop
for i in range(10):
    print('The value of the variable i is ' + str(i))
    

# priting stars
for i in range(10):
    print("*" * i)


# calculation inside for loop
balance = 1000
interest = 0.06
for i in range(30):
    balance = balance * (1+interest)
    print('The balance for this year is $' + str(balance))
