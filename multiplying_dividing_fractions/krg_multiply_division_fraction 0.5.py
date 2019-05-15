# Ryan K., Multiplying and Dividing Fractions, 05/05/2019,version 0.5

print("hello! My Name Is MathBot and I Will multiply and divide fractions.\n")
print("In Order to multiply fractions, you need too  know the numerator and denomerator of the fractions.")
user_name = input("what is your name?[Type your name and press ENTER.\n")
print("Hello,",user_name," how are you today?")

print("For this program, I need to know the numerator and the denominator for both fractions. \n")

# Variables for fraction 0.
numerator0= int(input("Type the first numerator and press enter. \n"))
denominator0= int(input("Type the first denominator and press enter. \n"))
print("The first fraction is", numerator0,"/",denominator0,".\n" )

# variables for fraction 1.
numerator1= int(input("Type the second numerator and press enter.\n"))
denominator1= int(input(" Tpe the second denominator and press enter.\n"))
print("The second fraction is", numerator1,"/",denominator1,".\n" )

print ("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", numerator1,"/",denominator1,".\n" )

# This is where the division of the fractions will start.

print("To divide a fraction, you need to multiply using the reciprocal or inverse of the seond fraction.\n")

new_numerator = numerator0 = denominator1
new_denominator = denominator0 = numerator1
print("The new fraction is", new_numerator,"/", new_denominator,".\n" )