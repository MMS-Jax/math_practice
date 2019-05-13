# Jayla L., Multiplying and Dividing Fractions, 05/06/2019, version 0.5

print("Hello, welcome to Fraction-Bot 9000.   I can multiply and divide fractions for you!\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello,", user_name,"how are you today?\n")

print ("For this program, I need to know the numerator and denomnator for both fractions.\n")

#Variable for fraction 0.
numerator0 = 0
denominator0 = 0
print("The first fraction is",numerator0,"/", denominator0, ". \n")

#Variables for frcation 1.
numerator1  = 0
denominator1 = 0
print("The second fraction is",numerator1,"/", denominator1, ". \n")

print("When mulitplying fractions you multiply the two numerators together. \n")
print("Then you multiply the two denomnators together. \n")

new_numerator =  numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is",new_numerator,"/",new_denominator, ". \n")

#This is where divding fractions start. 
print("Now I am going to divide a fraction for you. Please input your numerators and denominators.\n")
numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))


print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")


new_numerator = numerator0 * denominator1 
new_denominator =  numerator1 * denominator0

print("The new fraction is",new_numerator,"/",new_denominator, ". \n")

