# F to C temperature conversion function
def FtoC(tempF):
    tempC = (tempF - 32) * (5/9)
    return tempC

print(FtoC(-20))
print(FtoC(0))
print(FtoC(100))
