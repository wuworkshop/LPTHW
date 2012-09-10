# Defines the function cheese_and_crackers with 2 arguments
def cheese_and_crackers(cheese_count, boxes_of_crackers):
    # Inserts the variable cheese_count and prints the string
    print "You have %d cheeses!" % cheese_count
    # Inserts the variable boxes_of_crackers and prints the string
    print "You have %d boxes of crackers!" % boxes_of_crackers
    # Prints the string
    print "Man that's enough for a party!"
    # Prints the string
    print "Get a blanket.\n"

    
# Prints the string
print "We can just give the function numbers directly:"
# Calls the function and passes 2 numbers as parameters
cheese_and_crackers(20, 30)


# Prints the string
print "OR, we can use variables from our script:"
# Assigns the number to the variable amount_of_cheese
amount_of_cheese = 10
# Assigns the number to the variable amount_of_crackers
amount_of_crackers = 50

# Calls the function and passes 2 variables as parameters
cheese_and_crackers(amount_of_cheese, amount_of_crackers)


# Prints the string
print "We can even do math inside too:"
# Calls the function and passes 2 math values
cheese_and_crackers(10 + 20, 5 + 6)


# Prints the string
print "And we can combine the two, variables and math:"
# Calls the function and passes a combination of variables and math as 
# parameters
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)