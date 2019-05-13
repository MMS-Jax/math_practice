# Multiplying and Dividing Fractions By Daniel A. 05/06/19 Version 1.0

print("Welcome to the Math bot 6IX9INE I can MULTIPLY AND DIVIDE FRACTIONS!\n ")
user_name = input("What is your name? [type your name press ENTER.]\n ")
print("Hello," ,user_name,"How are you today?")

print("for this program,i need to know numerator and the denominator for both fractions.\n")

# variables for fraction 0
numerator0 = 0
denominator0 = 0
print("the fist fraction is", numerator0,"/", denominator0,".\n")

# Variables for fraction 1
numerator1 = 0
denominator1 = 0
print("the second fraction is", numerator1,"/", denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominaators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n"))
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("the new fraction is",new_numerator,"/", new_denominator ,".\n")

# This is where the division of the fractions will start. You will need to change this code!
pie = 22 / 7
print(pie)
print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")