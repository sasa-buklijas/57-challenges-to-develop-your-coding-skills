
total = float(raw_input("What is the order amount? "))
state = raw_input("What state do you live in? ").lower().strip()

if state == "wisconsin":
    
    country = raw_input("What country do you live in? ").lower().strip()

    if country == "eau claire":
        tax = 0.055
    elif country == "dunn":
        tax = 0.054
    else:
        tax = 0.05
        
    tax = total * tax
    print 'The tax is $%.2f.' % tax
    print 'The total is $%.2f.' % (tax + total)
    
elif state == "illinois":
    tax = total * 0.05
    print 'The tax is $%.2f.' % tax
    print 'The total is $%.2f.' % (tax + total)
    
else:
    print 'The total is $%.2f.' % total


