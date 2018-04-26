
length = raw_input("What is the length of the room in feet?  ")
width = raw_input("What is the width of the room in feet? ")

length_as_int = int(length)
width_as_int = int(width)

square_feet = length_as_int * width_as_int
square_meters = square_feet * 0.09290304

print "You entered dimensions of %s feet by %s feet." % (length, width)
print "The area is"
print "%d square feet" % square_feet
print "%.3f square meters" % square_meters
