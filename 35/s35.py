import random

l = []

while True:
    n = raw_input('Enter a name: ')

    if n == '':
        break
    else:
        l.append(n)

print 'The winner is... %s.' % random.choice(l)
