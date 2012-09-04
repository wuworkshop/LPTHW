from sys import argv

script, title, user_name = argv
prompt = '(^O^)/ '

print "Hello %s %s, I'm the %s script." % (title, user_name, script)
print "I'd like to ask you a few questions."
print "Do you like me %s?" % user_name
likes = raw_input(prompt)

print "Where do you live %s?" % user_name
lives = raw_input(prompt)

print "What kind of computer do you have?"
computer = raw_input(prompt)

print "Am I acting like a stalker?"
stalker = raw_input(prompt)

print """
Alright, so you said %r about liking me.
You live in %r. Not sure where that is.
And you have a %r computer. Nice.
Oh, and you said %r about me acting like
a stalker. Are you sure about that last
part?
""" % (likes, lives, computer, stalker)