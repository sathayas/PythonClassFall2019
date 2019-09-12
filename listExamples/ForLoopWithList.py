# For loop with a numerical list
minutes = [0, 15, 30, 45, 60, 75, 90, 105, 120]
for iMin in minutes:
    print('Elapsed time = ' + str(iMin))

# For loop with a string list
menu = ['Chili', 'Hot Dog', 'Salad', 'Tacos', 'Pizza']
for iMenu in menu:
    print("Today's special is " + iMenu)

# For loop with a range function
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
menu = ['Chili', 'Hot Dog', 'Salad', 'Tacos', 'Pizza']
for i in range(len(day)):
    print(day[i] + "'s special is " + menu[i])

# For loop with enumerate
day = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday']
menu = ['Chili', 'Hot Dog', 'Salad', 'Tacos', 'Pizza']
for i, iDay in enumerate(day):
    print(iDay + "'s special is " + menu[i])
