
print 'Press C to convert from Fahrenheit to Celsius.'
print 'Press F to convert from Celsius to Fahrenheit.'
leter = raw_input('Your choice: ').lower()

if leter == 'f':
    t = int(raw_input('Please enter the temperature in Fahrenheit: '))
    c = (t - 32) * 5.0/9.0
    print 'The temperature in Celsius is %d.' % c
else:
    t = int(raw_input('Please enter the temperature in Celsius: '))
    f = (t * 9.0/5.0) + 32
    print 'The temperature in Fahrenheit is %d.' % f

