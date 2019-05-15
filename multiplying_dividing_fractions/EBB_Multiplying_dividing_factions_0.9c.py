# Ethan B., Multiplying and Dividing Fractions, 05/06/2019, version 0.9c

print("Hello, welcome to the Fraction-Bomber 3000.   I will multiply and divide those hard fractions for you!\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello,", user_name,"how are you today?\n")

print("for this program, I will need to know the numerator and the denominator for both fractions.\n")

# Variables for fraction 0
numerator0 = 0
denominator0 = 0
print("The first fraction is",numerator0, "/", denominator0, ". \n" )

# Variables for fraction 1
numerator1 = 0
denominator1 = 0
print("The second fraction is",numerator1, "/", denominator1, ". \n" )

print("When mulitplying fractions you muliply the two numerators together. \n")
print("Then you will muliply the two denominators together. \n")

# Input the first fraction. 
numerator0 = int(input("Type the first numerator and press enter.\n")) 
denominator0 = int(input("Type the first denominator and press enter.\n"))

# Input the second fraction. 
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The Muliplyed fraction is",new_numerator, "/", new_denominator, ". \n" ) # Print the new fraction on the screen. 


# YOU NEED TO WRITE THE CODE TO PROPERLY DIVIDE THE TWO FRACTIONS.
# If you need help please see me.  I have an example on the board to help you. 

new_numerator = numerator0 * denominator1
new_denominator = numerator1 * denominator0

print("The Divided fraction is",new_numerator, "/", new_denominator, ". \n" ) # Print the new fraction on the screen. 
