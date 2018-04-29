
p1 = int(raw_input("Enter the price of item 1: "))
q1 = int(raw_input("Enter the quantity of item 1: "))
p2 = int(raw_input("Enter the price of item 2: "))
q2 = int(raw_input("Enter the quantity of item 2: "))
p3 = int(raw_input("Enter the price of item 3: "))
q3 = int(raw_input("Enter the quantity of item 3: "))

subtotal = (p1*q1) + (p2*q2) + (p3*q3)
tax = subtotal * 0.055
total = subtotal + tax

print "Subtotal: $%.2f" % subtotal
print "Tax: $%.2f" % tax
print "Total: $%.2f" % total
