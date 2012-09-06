# Imports the argv variable from the sys module
from sys import argv

# "Unpacks" argv and assigns it to the 2 variables on the left
script, filename = argv

# Opens the variable filename and returns a file object that's assigned
# to the variable txt
txt = open(filename)

# Inserts the variable filename into the string and prints the string
print "Here's your file %r:" % filename

# Runs txt's read function/method and prints the string that's returned
print txt.read()

# Prints the string
print "Type the filename again:"

# Assigns the value from raw_input to the variable file_again
file_again = raw_input(">")

# Opens the variable file_again and returns a file object that's assigned
# to the variable txt_again
txt_again = open(file_again)

# Runs txt_again's read function/method and prints the string that's returned
print txt_again.read()