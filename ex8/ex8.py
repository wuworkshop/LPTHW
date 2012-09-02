# Assigns the string to the variable formatter
formatter = "%r %r %r %r"

# Puts the numbers inside the variable formatter and
# prints them out
print formatter % (1, 2, 3, 4)

# Puts the strings inside the variable formatter and prints them out
print formatter % ("one", "two", "three", "four")

# Puts the boolean values inside the variable formatter and 
# prints them out
print formatter % (True, False, False, True)

# Puts 4 instances of the variable formatter inside the variable
# formatter and prints them out
print formatter % (formatter, formatter, formatter, formatter)

# Puts the strings inside the variable formatter and prints them out
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight."
)