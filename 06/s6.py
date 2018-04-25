
age = raw_input("What is your current age? ")
retire = raw_input("At what age would you like to retire? ")

import time
year = int(time.strftime("%Y"))
until = int(retire) - int(age)

print "You have %d years left until you can retire." % until
print "It's %d, so you can retire in %d." % (year, year + until)
