from math import log10 as log

b = float(raw_input("What is your balance? "))
apr = float(raw_input("What is the APR on the card (as a percent)? "))
p = float(raw_input("What is the monthly payment you can make? "))

i = apr /100.0 / 365

n = -1.0/30.0 * ( log (1 + b/p * (1 - (1 + i)**30 ) ) / log(1 + i) )

print 'It will take you %d months to pay off this card.' % n
