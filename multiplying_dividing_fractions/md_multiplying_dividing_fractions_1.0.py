# Mason D., Multiplying and Dividing Fractions, 5/6/2019, version 1.0

print("Hello! Welcome to lil Fraction- Over 9000. I Will Multiply and Divide your Fractions for You \n")
user_name = input ("what is your name? [Type your name and press ENTER.]\n")
print("Hello, ",user_name," how are you today? \n")

print("For this program, I need to know the numerator and denominator for both fractions. \n")

# Variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0,"/", denominator0, ".\n")

# Variables for fraction 1.
numerator1 = 0
denominator1 = 0
print("The second fraction is", numerator1,"/", denominator1, ".\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

# Input the first fraction
numerator0= int(input("Type the first numerator and press enter.\n")) 
denominator0 = int(input("Type the first denominator and press enter.\n"))

# Input the second fraction
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1 # Multiply the two numerators together. 
new_denominator = denominator0 * denominator1 # Multiply the two denominators together.

print("The new fraction is", new_numerator,"/",new_denominator,".\n") # Print the new fraction on the screen. 


print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")
   
print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is",numerator1,"/", denominator1,".\n")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))