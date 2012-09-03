tabby_cat = "\tI'm tabbed in."
persian_cat = "I'm split\non a line."
backslash_cat = "I'm \\ a \\ cat."

fat_cat = """
I'll do a list:
\t* Cat food
\t* Fishies
\t* Catnip\n\t* Grass
"""

print tabby_cat
print persian_cat
print backslash_cat
print fat_cat

single_quotes = '''
The remedy is an experience
It's just a dangerous liason
I won't worry my life away
Aaaaay, oooooh
'''

# Extra Credit
print single_quotes
print u"100\u0025"
print u"\N{dollar sign}1,000"
print "Format string r - %r %r" % ('how\'s that?', "you\"ll get it.")
print "Versus s - %s %s" % ('how\'s that?', "you\"ll get it.")
print "%s" % "So I said \"don't ya\"ll get it?!?\""

# For fun. Hit Ctrl-c to kill it.
while True:
    for i in ["/","-","|","\\","|"]:
        print "%s\r" % i,
