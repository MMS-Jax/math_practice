# Nicolas D., Multiplying and Dividing Fraction, version 0.9

print("This program is used to multiply and divide fractions.\n")

user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello",user_name,"how are you today")

print("For this program, I need the numerator and the denominator of both fractions.\n")
# Variables for fraction 0
numerator0 = int(input("[Type the first numerator and press ENTER.]\n"))
denominator0 = int(input("[Type the first denominator and press ENTER.]\n"))
print("The first fraction is", numerator0,"/",denominator0,".\n")

# Variables for fraction 1
numerator1 = int(input("[Type the second numerator and press ENTER.]\n"))
denominator1 = int(input("[Type the second denominator and press ENTER.]\n"))
print("The second fraction is", numerator1,"/", denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you multiply the two denominators together.\n")

new_numerator   = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/", new_denominator 
,".\n")

# This is where divison starts
print("To dived a fraction you will multiply using the reciprocal of the second fraction.\n")
div_new_numerator = numerator0 * denominator1
div_new_denominator = denominator0 * numerator1

print("The divided fraction is", div_new_numerator,"/", div_new_denominator 
,".\n")