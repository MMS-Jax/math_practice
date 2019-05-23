# Jacob O., Multiplying and Dividing Fractions, 05/14/2019, version 0.2

print("What's up G, I can multiplay and divide fractions for you instead of you getting frustrated in math class.\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("What's up", user_name, "How are you today?\n" )

print("for this program, I need to know the numerator and the denominator for both fractions.\n")

#variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("The first fraction is",numerator0,"/",denominator0,".\n")

#variables for fraction 1.
numerator1 = 0
denominator1 = 0
print("The second fraction is",numerator1,"/",denominator1,".\n")

print("When multiplying fractions you multiply the two numertors together.\n")
print("Then you will multiply the two denominators together.\n")

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

print("The new fraction is",new_numerator,"/",new_denominator,".\n") # Print the new fraction on the screen. 

print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")

new_numerator = numerator0 * denominator1
new_denominator = numerator1 * denominator0

print("The divided fraction is",new_numerator, "/", new_denominator,". \n") # print the new fraction on the screen

print("When you divided the fractions, you multiplied by the reciprocal or the inverse of the second fraction. \n ")

print("Your welcome mr or mrs (im not judging) for multiplying and dividing your fractions instead of using a pesky calculator, come back soon. \n") 