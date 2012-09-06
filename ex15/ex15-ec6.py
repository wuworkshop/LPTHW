from sys import argv

filename = raw_input("Name of file to open: ")

txt = file(filename, 'a')

txt.write("""
This file was created using file's write method.
Neato!
""")
txt.close()

print "Here's your file %r:" % filename

txt_again = file(filename)
print txt_again.read()


