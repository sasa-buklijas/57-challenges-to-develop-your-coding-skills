
amount_from = int(raw_input("How many euros are you exchanging? "))
rate_from = float(raw_input("What is the exchange rate? "))

rate_to = 82 # hard-coded 82 euros for 100 USD
amount_to = (amount_from * rate_from) / rate_to

print "%d euros at an exchange rate of %.2f is %f U.S. dollars." % (amount_from, rate_from, amount_to)
