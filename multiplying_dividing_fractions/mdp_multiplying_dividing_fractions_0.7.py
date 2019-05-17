# Marrio P., Multiplying and fractions 05/06/2019, version 0.7

print("Hello, welcome to Fraction-Bot 1000.  I can mulitply and divide fractions for you!\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello,", user_name,"how are you today?")

print("For this program, I need to know the numerator and the denominator for both fractions.\n")

# Varaibles for fraction 0.
numerator0 = 0
denominator0 =  0
print("The first fraction is",numerator0,"/",denominator0,".\n")

# Varaibles for fraction 1.
numerator1 = 1
denominator1 = 1
print("The second fraction is",numerator1,"/",denominator1,".\n")

print("When multipying fractions you multiply the two numerators together")
print("Then you will multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = numerator0 * denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")

# This is where the division of the fractions will start. You will need to change this code!

print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")\

# Varaibles for fraction 3.
numerator1 = 1
denominator1 = 0

numerator1 = int(input("Type the second numerator and press enter.\n")) 
numerator0 = int(input("Type the first numerator and press enter.\n"))

print("The thrid fraction is",numerator1,"/",denominator0,".\n")

new_numerator = numerator1 * numerator1
new_denominator = numerator1 * denominator0
