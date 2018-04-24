
first = raw_input("What is the first number? ")
second = raw_input("What is the second number? ")
first_as_int = int(first)
second_as_int = int(second)

print "%s + %s = %d" % (first, second, first_as_int + second_as_int)
print "%s - %s = %d" % (first, second, first_as_int - second_as_int)
print "%s * %s = %d" % (first, second, first_as_int * second_as_int)
print "%s / %s = %d" % (first, second, first_as_int / second_as_int)
