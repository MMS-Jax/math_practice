# Sheyna W., Multiplying and Dividing Fractions, 05/06/19, Version 0.3

print("Hello, my name is Dr. Phil the Fraction God, and I was made to consult you on multiplying and dividing fractions. Nice to meet you.\n ")
user_name = input("First, I need to know what your name is. Please type it into the space provided. [Type your username and press ENTER.] \n")
print("Welcome to the Ranch,", user_name, ".")

print("In order to multiply and divide fractions for you, sir or madam, I need to know both the numerator and denominator of your fractions.\n")

# Variables for Fraction 0.
numerator0 = 0
denominator0 = 0

# Variables for Fraction 1.
numerator1 = 0
denominator1 = 0


print("To multiply fractions, you multiply the numerators together.\n")
print("After that, you'll multiply the denominators together. Yeet.\n")

numerator0 = int(input("Please type in the first numerator and press ENTER.\n"))
numerator1 = int(input("Please type in the second numerator and press ENTER.\n"))

denominator0 = int(input("Please type in the first denominator and press ENTER.\n"))
denominator1 = int(input("Please type in the second denominator and press ENTER.\n"))

print("The first fraction is,", numerator0,"/",denominator0,".\n" )
print("The second fraction is," , numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is,", new_numerator,"/", new_denominator,".\n")

print("Good job,", user_name, ", you aren't a complete failure. I'm sincerely proud of you.")

# This is where the division of fractions will start.

pie = 22 / 7

print(pie)

print("When you work to divide fractions, you multiply using the reciprocal, or the inverse of the second fraction.\n")

numerator0 = int(input("Please type in the first numerator and press ENTER.\n"))
numerator1 = int(input("Please type in the second numerator and press ENTER.\n"))

denominator0 = int(input("Please type in the first denominator and press ENTER.\n"))
denominator1 = int(input("Please type in the second denominator and press ENTER.\n"))

new_numerator = denominator0 * numerator1
new_denominator = numerator0 * denominator1

print("The new fraction is,", new_numerator,"/", new_denominator,".\n")