# Alani S., Multipling and Dividing Fractions, 05/06/2019, version 1.0

print("Hello, welcome to Fraction-Bot 9000.  I can multiply and divide fractions for you!\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello," , user_name,"how are you today?\n")

print("For this program, I need to know the numerator and the denominator for both fractions.\n")

# Variables for fraction  0.
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0,"/",denominator0,".\n")

# Variables for fractions 1.
numerator1 = 0
denominator1 = 0
print("The second fraction is",numerator1,"/",denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n"))
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is",numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

#  This is where the division of the fraction will start. you will need to change this code!
print("To divide a fraction, you will multiply using the reciprical or inverse of the second fraction.\n")

new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")

print("In order to divide fractions you will need to, keep the first fraction the same and change the division sign to a multiplication sign and then flip the second fraction by putting the denominator where the numerator was and put the numerator where the denominater was.\n")