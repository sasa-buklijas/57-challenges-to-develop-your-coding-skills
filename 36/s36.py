
def standard_deviation(l):
    mean = sum(l)/len(l)

    li = []
    for n in l:
        li.append( (mean - n)**2 )

    a = sum(li)/len(li)

    return a**0.5


l = []

while True:
    n = raw_input('Enter a number: ')

    if n == '':
        break
    else:
        l.append(int(n))

print 'Numbers: %s.' % l

print 'The average is %.2f.' % (sum(l)/len(l))
print 'The minimum is %d.' % min(l)
print 'The maximum is %d.' % max(l) 
print 'The standard deviation is %.2f.' % standard_deviation(l)
