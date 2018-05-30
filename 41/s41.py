from operator import itemgetter


l = []
with open("in.txt", "r") as f:
    for line in f:
        t = line.split(',')
        l.append({'fn': t[0].strip(), 'ln': t[1].strip()})

data = sorted(l, key=itemgetter('fn'))

with open("out.txt", "w") as f:
    f.write('Total of %d names\n' % len(data))
    f.write('-----------------\n')
    for i in data:
        f.write('{fn}, {ln}\n'.format(**i))
