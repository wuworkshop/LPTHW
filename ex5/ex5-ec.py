name = 'Zed A. Shaw'
age = 35 # not a lie
height = 74 # inches
weight = 180 # lbs
eyes = 'Blue'
teeth = 'White'
hair = 'Brown'
height_in_cm = height * 2.54 # 1 inch = 2.54 cm
weight_in_kg = weight * 0.4536 # 1 lb = 0.4536 kg 

print "Let's talk about %s." % name
print "He's %d inches tall." % height
print "He's %d pounds heavy." % weight
print "Actually that's not too heavy."
print "He's got %s eyes and %s hair." % (eyes, hair)
print "His teeth are usually %s depending on the coffee." % teeth

# this line is tricky, try to get it exactly right
print "If I add %d, %d, and %d I get %d." % (age, height, weight, age + height + weight)

print "His weight in kilos is %r." % weight_in_kg
print "His height in centimeters is %g." % height_in_cm