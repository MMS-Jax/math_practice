# Richardson A., Multiplying Dividing Fractions 05/15/19 version 0.7

print("Hello. I am Fraction Bot 9000.   I can multiply and divide fractions for you!\n")
user_name = input("Please state your name [Type Your Name And Press Enter.]")
print("Hello,", user_name, "how are you today?\n")

print("For this program, I need to know the numerator and denominator for both fractions.\n")

# Variables for fraction 0
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0, "/", denominator0,".\n")

# Variables for fraction 1 
numerator1 = 0
denominator1 = 0
print("The second fraction is", numerator1, "/", denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together. \n")
# Input the first fraction. 
numerator0 = int(input("Type the first numerator and press enter.\n")) 
denominator0 = int(input("Type the first denominator and press enter.\n"))

# Input the second fraction. 
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1 # Multiply the two numerators together. 
new_denominator = denominator0 * denominator1 # Multiply the two denominators together.

print("The new fraction is", new_numerator,"/",new_denominator,".\n") # Print the new fraction on the screen. 

# This is where the division of the fractions will start.

print("To divide a fraction,you will multiply the reciprocal or inverse of the second fraction.\n")

new_numerator = numerator0 * denominator1 # Multiply the two numerators together. 
new_denominator = denominator0 * numerator1 # Multiply the two denominators together.

print("The new fraction is", new_numerator,"/",new_denominator,".\n") # Print the new fraction on the screen.
