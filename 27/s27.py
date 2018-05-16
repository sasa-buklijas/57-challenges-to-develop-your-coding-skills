import re

fn = raw_input("Enter the first name: ")
ln = raw_input("Enter the last name: ")
code = raw_input("Enter the ZIP code: ")
eid = unicode(raw_input("Enter an employee ID: "))
# unicode because of eid.isnumeric()

if fn == '' or not fn.isalpha() or len(fn) <=2:
    print 'First name not correct'

if ln == '' or not ln.isalpha() or len(ln) <=2:
    print 'Last name not correct'

if not re.match(r'^[A-Z]{2}-[0-9]{4}$', code):
    print 'ZIP code not correct'

if not eid.isnumeric():
    print 'Employee ID name not correct'
