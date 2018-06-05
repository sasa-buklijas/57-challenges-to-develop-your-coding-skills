import urllib, json


url = 'http://api.open-notify.org/astros.json'
response = urllib.urlopen(url)
data = json.loads(response.read())

n = data['number']

print 'There are %d people in space right now:' % n
print
print 'Name                | Craft'
print '--------------------|------'
for i in data['people']:
    print '{name:19} | {craft}'.format(**i)



