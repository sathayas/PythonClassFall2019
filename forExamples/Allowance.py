allowance = 1  # start out with $1
for i in range(24):
    print('Month ' + str(i+1) + ':  $' + str(allowance))
    allowance = allowance * 2  # doubled for next month
