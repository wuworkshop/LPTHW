from sys import argv

script, filename = argv

txt = open(filename)

print "Here's the file: ", filename
print txt.read()

