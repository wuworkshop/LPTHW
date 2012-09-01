# The number 10 is put inside the string and
# the string is assigned to the variable x
x = "There are %d types of people." % 10

# Assigns the string to the variable binary
binary = "binary"

# Assigns the string to the variable do_not
do_not = "don't"

# The 2 variables binary and do_not are put inside the 
# string and the string is assigned to the variable y
y = "Those who know %s and those who %s." % (binary, do_not)

# Prints the variable x
print x

# Prints the variable y
print y

# The variable x is put inside the string and printed
print "I said %r." % x

# The variable y is put inside the string and printed 
print "I also said: '%s'." % y

# Assigns False to the variable hilarious
hilarious = False

# Assigns the string to the variable joke_evaluation
joke_evaluation = "Isn't that joke so funny?! %r"

# Puts the variable hilarious inside the variable joke_evaluation
print joke_evaluation % hilarious

# Assigns the string to the variable w
w = "This is the left side of..."

# Assigns the string to the variable e
e = "a string with a right side."

# Concatenates the two variables w and e 
print w + e