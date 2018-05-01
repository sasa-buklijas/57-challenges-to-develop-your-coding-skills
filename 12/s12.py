
principal = int(raw_input("Enter the principal: "))
interest_rate = float(raw_input("Enter the rate of interest: "))
years = int(raw_input("Enter the number of years: "))

amount = principal * (1 + ( interest_rate/100 * years))

print
print "After %d years at %.2f%%, the investment will be worth $%f." % (years, interest_rate, amount)
