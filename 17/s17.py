
weight = int(raw_input("What is your weight? "))
oz = int(raw_input("How many ounces of alcohol did you have? "))
since_last_drink = int(raw_input("What amount of time since your last drink? "))
gender = raw_input("What is your gender [m or f]? ")

if gender == 'm':
    r = 0.73
else:
    r = 0.66

bac = (oz * 5.14 / weight * r) - 0.015 * since_last_drink

print 'Your BAC is %f' % bac
if bac >= 0.08:
    print 'It is not legal for you to drive.'
else:
    print 'It is legal for you to drive.'
