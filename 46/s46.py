import collections
from operator import itemgetter


data = open('words.txt', 'r').read().split()

count = collections.Counter(data)
count_sorted = collections.OrderedDict(count.most_common())

for k, v in count_sorted.iteritems():
    print '{key:8}: {value}'.format(key=k, value=v * '*')
