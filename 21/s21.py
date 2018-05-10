
n = int(raw_input("Please enter the number of the month: "))

months = {
    1: 'January',
    2: 'February',
    3: 'March',
    4: 'April',
    5: 'May',
    6: 'June',
    7: 'July',
    8: 'August',
    9: 'September',
    10: 'October',
    11: 'November',
    12: 'December',
    }

name = months.get(n, 'ERROR - number too large')

print 'The name of the month is %s.' % name
