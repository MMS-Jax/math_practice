# Multiplying and Dividing fractions Elena G. 5/6/19 version 1.1

print ("Welcome I am Multiplying-Bot 3000. I can Multiply and Divide fractions for you. \n")
user_name = input("what is your name? [Type your name and press ENTER.  ]\n")
print ("Hello ", user_name,"how are you today?")

print("For this program, I need to know the numerator and denominator for both fractions. \n")

# Variables for fraction 0.
numerator0 = 0
denominator0 = 0
print(" The first fraction is",numerator0, "/",denominator0, ".\n" )

# variables for fraction 1.
numerator1 = 0
denominator1 = 0
print("The second fraction is",numerator1, "/" ,denominator1,  ".\n" )

print("When multiplying fractions you multiply the two numerators together.\n")
print("The you will also multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n"))
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1= int(input("Type the second  denominator and press enter.\n"))

print("The first fraction is", numerator0,"/", denominator0, ".\n")
print("The second fraction is", numerator1,"/", denominator1, ".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("the new fraction is", new_numerator,"/", new_denominator, ".\n" )

#This is where the division of the fraction will start.You will need to change this code!  


print("To divide a fraction, you will flip the second fraction. And then multiply both fractions together. .\n")

print("the new fraction is", new_numerator,"/", new_denominator, ".\n" )

numerator0 = int(input("Type the second   numerator and press enter.\n"))
numerator1 = int(input("Type the first numerator and press enter.\n"))

denominator0 = int(input("Type the second  denominator and press enter.\n"))
denominator1= int(input("Type the first  denominator and press enter.\n"))

print("the new fraction is", new_numerator,"/", new_denominator, ".\n" )

new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1 

print("the new fraction is", new_numerator,"/", new_denominator, ".\n" )


  
























