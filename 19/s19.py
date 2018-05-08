
weight = float(raw_input('Please enter your weight: '))
height = float(raw_input('Please enter your height: '))

bmi = (weight / (height * height)) * 703

print 'Your BMI is  %.2f.' % bmi
if bmi <= 18.5:
    print 'You are underweight. You should see your doctor.'
elif bmi >= 25.0:
    print 'You are overweight. You should see your doctor.'
else:
    print 'You are within the ideal weight range.'

