# Powell C., Multiplying and Divide Fractions, 05/06/2019 Ver 0.9

print("Hello, my name is Youngmathboi. I will multiply and divide fractions for you.\n")
user_name = input("What is your name? [Type your name and press ENTER.\n")
print("Hello,", user_name,"how are you today?\n")
print("In order for me to do that i need to know the numerator and the denominator of the equation.\n")


# Variables for Fraction 0.
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0,"/", denominator0,".\n")

# Variables for Fraction 1
numerator1 = 0
denominator1 = 0
print("The second fraction is", numerator1,"/", denominator1,".\n")

print("When multpiplying fractions together you multiply the two numerators together.\n")
print("Then you must multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n"))
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/", new_denominator,".\n")

new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1

# This is where the division of the Fractions will start.

print("To divide fraction you need to multiply the reciprocal or the opposites together.\n")

new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1

print("Thank you for using youndashboimath Problem solver!!\n")