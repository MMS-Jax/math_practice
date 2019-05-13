# kasey.c, Multiplying and Dividing Fractions, 05/10/2019, version 0.8

print("Hello, welcome to Fraction-Bot 900.   I can multiply and divide fractions for you!\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello,", user_name,"how are you today?\n")

print("For this program, I need to know the numerator and the denominator for both fractions.\n")

# Variables for fraction 0. 
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0,"/",denominator0,".\n")

# Variables for fraction 1. 
numerator1 = 0
denominator1 = 0
print("The second fraction is", numerator1,"/",denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator =  numerator * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")

print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")
numerator0 * denominator1
numerator1 * denominator0
print("The new fraction is", new_numerator,"/",new_denominator,".\n"