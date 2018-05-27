
l = raw_input("Enter a list of numbers, separated by spaces: ")

l = l.strip().split()

even = []
for i in l:
    if int(i) % 2 == 0:
        even.append(i)

print 'The even numbers are %s.' % even
