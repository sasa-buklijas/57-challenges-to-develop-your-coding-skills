
e = ['John Smith', 'Jackie Jackson', 'Chris Jones', 'Amanda Cullen', 'Jeremy Goodwin']

for i in e:
    print i
print

r = raw_input('Enter an employee name to remove: ')

e.remove(r)

for i in e:
    print i
print
