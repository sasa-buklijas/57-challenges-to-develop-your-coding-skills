
people = raw_input("How many people? ")
pizzas = raw_input("How many pizzas do you have? ")
slices_per_pizza = raw_input("How many number of slices per pizza? ")

people_as_int = int(people)
pizzas_as_int = int(pizzas)
slices_per_pizza_as_int = int(slices_per_pizza)

sum_slices = pizzas_as_int * slices_per_pizza_as_int
slice_per_person =  sum_slices / people_as_int
leftover = sum_slices % people_as_int   

print
print "%s people with %s pizzas, with %s slices per pizza" % (people, pizzas, slices_per_pizza)
print "Each person gets %d pieces of pizza." % slice_per_person
print "There are %d leftover pieces." % leftover
