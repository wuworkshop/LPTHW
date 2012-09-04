from sys import argv

script, q1, q2, q3 = argv

print "The script is called:", script
print "Your age:", q1
print "Your birthplace:", q2
print "Gender:", q3

name = raw_input("What is your name? ")
print "Your name is %s. You are %s years old and you were born in %s." % 
(name, q1, q2)