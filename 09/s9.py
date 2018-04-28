
length = raw_input("What is length? ")
width = raw_input("What is width? ")

area = int(length) * int(width)
import math
galons = math.ceil(area / 350.0)

print
print "You will need to purchase %d gallons of paint to cover %d square feet." % (galons, area)
