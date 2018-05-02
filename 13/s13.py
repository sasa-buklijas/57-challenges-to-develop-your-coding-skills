
p = int(raw_input("What is the principal amount? "))
r = float(raw_input("What is the rate? "))
t = int(raw_input("What is the number of years? "))
n = int(raw_input("What is the number of times the interest is compounded per year? "))

A = p * (1 + (r/100/n))**(n*t)

print
print "$%d invested at %.2f%% for %d years compounded %d times per year is $%.2f." % (p, r, t, n, A)
