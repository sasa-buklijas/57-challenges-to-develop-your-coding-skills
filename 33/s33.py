import random

a = ['Yes', 'No', 'Maybe', 'Ask again later.']
while True:
    s = raw_input('What\'s your question? ')

    if s == 'stop':
        break
    else:
        print '%s' % random.choice(a)
