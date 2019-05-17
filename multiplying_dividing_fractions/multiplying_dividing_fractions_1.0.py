# Multiplying and Dividing Fractions by Skylar C. 5/06/19 version 1.0

print("Welcome to the Fraction Calculator! I can multiply and divide fractions for you.\n" )
user_name = input("What is your name? [Type your name and press ENTER.] \n")
print("Welcome,", user_name,"How has your day been? ")

print("In order to run the program, I need to know the numerator and denomenator for both fractions. \n" )

# Variables for fraction 0.
numerator0 = 0
denomenator0 = 0
print("The first fraction is", numerator0, "/", denomenator0,".")
# Variables for fraction 1.
numerator1 = 0
denomenator1 = 0
print("The second fraction is", numerator1, "/", denomenator1,".")

print("When multiplying fractions you must multiply the two numerators together first. \n" )
print("Then you must multiply the two denomenators together. \n ")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denomenator0 = int(input("Type the first denominator and press enter.\n"))
denomenator1 = int(input("Type the second denominator and press enter.\n"))

new_numerator = numerator0 * numerator1
new_denomenator = denomenator0 * denomenator1

print("The new fraction is", new_numerator,"/", new_denomenator, ".\n")

# This is where the divison of the fractions will start.

print("To divide a fraction, you will multiply using the reciprocal or the inverse of the second fraction. \n")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denomenator0 = int(input("Type the first denominator and press enter.\n"))
denomenator1 = int(input("Type the second denominator and press enter.\n"))

new_numerator = numerator0 * denomenator1
new_denomenator = denomenator0 * numerator1

print("The new fraction is", new_numerator,"/", new_denomenator, ".\n")
