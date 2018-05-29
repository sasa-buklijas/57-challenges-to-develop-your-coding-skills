
data = [
{'fn' : 'John',      'sn':'Johnson',    'p':'Manager',           'sd':'2016-12-31'},
{'fn' : 'Tou',       'sn':'Xiong',      'p':'Software Engineer', 'sd':'2016-10-05'},
{'fn' : 'Michaela',  'sn':'Michaelson', 'p':'District Manager',  'sd':'2015-12-19'},
{'fn' : 'Jake',      'sn':'Jacobson',   'p':'Programmer',        'sd':''},
{'fn' : 'Jacquelyn', 'sn':'Jackson',    'p':'DBA',               'sd':''},
{'fn' : 'Sally',     'sn':'Weber',      'p':'Web Developer',     'sd':'2015-12-18'},
]

s = raw_input('Enter a search string: ')

print 'Name                | Position          | Separation Date'
print '--------------------|-------------------|----------------'
for i in data:
    name = i['fn'] + ' ' + i['sn']
    if name.find(s) != -1:
        print '{name:19} | {p:17} | {sd}'.format(name=name, **i)
