from operator import itemgetter


print 'Last     First     Salary'
print '-------------------------'

with open("in.txt", "r") as f:
    for line in f:
        t = line.split(',')
        print '{:8} {:9} {}'.format(t[0], t[1], t[2].strip())

