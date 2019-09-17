def metricConvert(feet, inch):
    lenMetric = 30.48*feet + 2.54*inch
    m = int(lenMetric//100)
    cm = lenMetric % 100
    return m, cm

mLen, cmLen = metricConvert(5,7)
print(str(mLen) + 'm ' + str(cmLen) + 'cm')
