import os

s = raw_input('Site name: ')
a = raw_input('Author: ')
y = raw_input('Do you want a folder for JavaScript? ')
c = raw_input('Do you want a folder for CSS? ')

print 'Created ./%s' % s
os.mkdir(s)

print 'Created ./%s/index.html' % s
with open(s + '/index.html',"w") as f:
    t="""
<!doctype html>

<html lang="en">
<head>
  <meta charset="utf-8">

  <title>{title}</title>
  <meta name="{author}">

<body>
  <h1>Hello</h1>
</body>
</html>
"""
    ft = t.format(title=s, author=a)
    f.write(ft)
    
if y == 'y':
    print 'Created ./%s/js/' % s
    os.mkdir(s + '/js/')

if c == 'y':
    print 'Created ./%s/css/' % s
    os.mkdir(s + '/css/')
