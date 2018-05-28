from operator import itemgetter


data = [
{'fn' : 'John',      'sn':'Johnson',    'p':'Manager',           'sd':'2016-12-31'},
{'fn' : 'Tou',       'sn':'Xiong',      'p':'Software Engineer', 'sd':'2016-10-05'},
{'fn' : 'Michaela',  'sn':'Michaelson', 'p':'District Manager',  'sd':'2015-12-19'},
{'fn' : 'Jake',      'sn':'Jacobson',   'p':'Programmer',        'sd':''},
{'fn' : 'Jacquelyn', 'sn':'Jackson',    'p':'DBA',               'sd':''},
{'fn' : 'Sally',     'sn':'Weber',      'p':'Web Developer',     'sd':'2015-12-18'},
]

data = sorted(data, key=itemgetter('sn'))

print 'Name                | Position          | Separation Date'
print '--------------------|-------------------|----------------'
for i in data:
    name = i['fn'] + ' ' + i['sn'] 
    print '{name:19} | {p:17} | {sd}'.format(name=name, **i)
