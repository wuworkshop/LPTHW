﻿from sys import argv

script, filename = argv

txt = open(filename)

print "Here's your file %r:" % filename
print txt.read()

txt.close()
print "Is txt closed?", txt.closed

print "Type the filename again:"
file_again = raw_input(">")

txt_again = open(file_again)

print txt_again.read()

txt_again.close()
print "Is txt_again closed?", txt.closed