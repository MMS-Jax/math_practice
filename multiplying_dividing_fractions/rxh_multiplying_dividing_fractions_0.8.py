#Roman H, Multiplying and Dividing Fractions, 05/15/2019, version 0.7

print("Hey, i'm the fraction man, I do the stuff with multiply and divide the fraction.\n")

user_name = input("You gotta name? [type it in then press ENTER.]\n")

print("Yo, ", user_name,"whats good?")

print("Ok, so I'm gonna need the numerator and the denominator for both fractions.\n")

# Input the first fraction. 
numerator0 = int(input("Type the first numerator and press enter.\n")) 
denominator0 = int(input("Type the first denominator and press enter.\n"))

# Input the second fraction. 
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

# Variables for fraction 0
numerator0 = 0
denominator0 = 0
print("The first fraction is" , numerator0, "/",denominator0, ".\n")

# Variables for fraction 1
numerator1 = 0
denominator1 = 0
print("The second fraction is" , numerator1, "/",denominator1, ".\n")

print("When you multiply the fractions, you gotta multiply the two numerators together.\n")
print("Then you multiply the two denominators together.\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("Your new fraction is", new_numerator, "/" ,new_denominator, ".\n")

# This is where the division of the fractions will start.

print("To divide the fraction, you gotta multiply using the reciprocal or inverse of the second fraction. \n")

new_numerator = denominator0 * numerator1
new_denominator = numerator0 * denominator1

print("Your new fraction is", new_numerator, "/" ,new_denominator, ".\n")