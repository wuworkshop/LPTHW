from sys import argv

filename = raw_input("Name of file to open: ")

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()
