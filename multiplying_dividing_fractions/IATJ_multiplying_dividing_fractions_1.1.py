# Isaac J., Multiplying and Dividing Fractions, 05/06/2019, version 1.0

print("Hello, welcome to Fraction-Bot 9000.   I can multiply and divide fractions for you!\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello,", user_name,"how are you today?\n")

print("For this program, I need to know the numerator and the denominator for both fractions.\n")

# Variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0,"/", denominator0,".\n")

# Variables for fraction 1.
numerator1 = 0
denominator1 = 0
print("The second fraction is", numerator1,"/", denominator1,".\n")

print("When you multiply the numerators together.\n")
print("Then you will multiply the two denominaotrs together.\n ")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n ")

# This is where the division of the fractions will start.
pie = 22 / 7
print(pie)
print("To divide a fraction, you will multiply using the reciprocal or inversde of the second fraction.\n")
new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n ")