#Multiplying and dividing fractions by Logan E. Version 4.0

print("Hello, welcome to fraction calculator 1234. I will multiply and divide fractios for you.\n")
user_name = input("What is your name? [Type your name and press enter]\n")
print("Hello,", user_name,"I hope you are having a good day.\n")

print("To start multiplying and dividing, I need to know the numerator and the denominator.\n")

# Variables for fraction 0
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0,"/",denominator0,".\n")

# Variables for fraction 1 (You can change these freely)
numerator1 = 1
denominator1 = 2
print("The second fraction is", numerator1,"/",denominator1,".\n")

print("When multiplying fractions, you multiply the two numerators together.\n")

print("After this you will multiply the two denominators together.\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")

# This is where the division of fractions will start.

print("To divide fractions, you will multiply using the reciprocal or inverse of the second fraction.\n")

new_numerator1 = numerator0 * denominator1
new_denominator1 = denominator0 * numerator1

print("The new divided fraction is", new_numerator1,"/",new_denominator1,".\n" )
