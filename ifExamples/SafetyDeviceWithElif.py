weight = float(input('Please enter your weight (pounds): '))
height = float(input('Please enter your height (inches): '))
if (weight<=300) and (height<=78):
    print('Requirements met!')
elif weight<=300:
    print('Weight requirement met!')
elif height<=78:
    print('Height requirement met!')
else:
    print('Neither requirement met!')
