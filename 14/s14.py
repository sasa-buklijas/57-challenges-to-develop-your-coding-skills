
total = int(raw_input("What is the order amount? "))
state = raw_input("What is the state? ")

if state == 'WI':
    sub_total = total
    tax = sub_total * 0.055
    total = tax + sub_total
    
    print "The subtotal is $%.2f" % (sub_total)
    print "The tax is $%.2f" % (tax)

print "The total is $%.2f" % (total)
