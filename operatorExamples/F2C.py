# input of temperature in Fahrenheit
tempF = int(input('What is the temperature [F]? '))
# the formula for conversion
tempC = (tempF - 32) * 5 / 9
# the output
print('The temperature is ' + str(tempC) + ' Celsius.')
