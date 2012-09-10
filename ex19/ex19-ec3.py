def area(h, w):
    return h * w

    
print "1. Give the function numbers directly:"
print area(20, 30)


print "2. Use variables from our script:"
height = 100
width = 125
print area(height, width)


print "3. Do math inside:"
print area(10 + 20, 20 + 15)


print "4. Combine the two, variables and math:"
print area(height + 10, width + 1000)


print "5. Ask the user for values:"
user_height = int(raw_input("Height? "))
user_width = int(raw_input("Width? "))
print area(user_height, user_width)


print "6. Combine asking the user for values and math:"
user_math_height = int(raw_input("Height? ")) + 200
user_math_width = int(raw_input("Width? ")) + 230
print area(user_math_height, user_math_width)


print "7. Use variables that use the function:"
func_w = area(100, 200)
func_h = area(20, 15)
print area(func_w, func_h)


print "8. Use variables that use the function with math:"
math_w = area(15, 35) + 200
math_h = area(28, 100) + 111
print area(math_w, math_h)


print "9. Use variables that use the function and variables:"
var_w = area(22, 35) + func_w
var_h = area(99, 121) + func_h
print area(var_w, var_h)


print "10. Use the function as parameters:"
print area(area(35,40), area(90, 100))

