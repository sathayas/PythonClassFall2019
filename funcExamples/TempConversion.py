# F to C temperature conversion function
def FtoC(tempF):
    tempC = (tempF - 32) * (5/9)
    return tempC

print(FtoC(-20))
print(FtoC(0))
print(FtoC(100))


# F to C temperature conversion function, returning both temperatures
def FtoC_ReturnBoth(tempF):
    tempC = (tempF - 32) * (5/9)
    return tempC, tempF


C, F = FtoC_ReturnBoth(90)
print(str(F) +' degree Fahrenheit = '+ str(C) +' degree Celsius')
