# Ryan Kelley, Multiplying and Dividing Fractions, 02/27/2020, version 1.0
import time 
print("Hello, welcome to Fraction-Bot 9000.   I can multiply and divide fractions for you!\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello",user_name,",how are you today?\n")
print("For this program, I need to know the numerator and the denominator for both fractions.\n")
time.sleep(5)

# Create and initialize the numerator and denominator variables.  
numerator0 = 0
denominator0 = 0
numerator1 = 0
denominator1 = 0

# Create a variable to store the user answer when checking student calculations.  
user_answer = 0

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")
time.sleep(5)

# Input the first fraction. 
print("Next you will input the values for the first fraction.")
numerator0 = int(input("Type the first numerator and press enter.\n")) 
denominator0 = int(input("Type the first denominator and press enter.\n"))
print("The first fraction is", numerator0,"/",denominator0,".\n")
time.sleep(5)

# Input the second fraction. 
print("Now you are going to input the values for the second fraction.")
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))
print("The second fraction is", numerator1,"/",denominator1,".\n")
time.sleep(5)

# Multiply the numerators.   
print("Ok, let me multiply the two numerators together...Give me a second!")
print("Can you double check my math?  Calculate the answer too, please.")
time.sleep(2)
user_answer = int(input("What did you calculate for the numerator?")
new_numerator = numerator0 * numerator1 
 
if user_answer == new_numerator:
	print("Great, I calculated",new_numerator,"as well.  Good math skills!")
else: 
	print("I got a different answer.  Please recalculate your answer.")
	user_answer = int(input("What did you calculate for the numerator this time?")
	if user_answer == new_numerator:
		print("Great, I calculated",new_numerator,"as well.  Good math skills!")
	else: 
		print("Something seems to be wrong.  It might be necessary to rerstart this program.")
		exit()
time.sleep(2)

# Multiply the denominators.
print("Ok, let me multiply the two numerators together...Give me a second!")
print("Can you double check my math?  Calculate the answer too, please.")
time.sleep(2)
user_answer = int(input("What did you calculate for the numerator?")
new_denominator = denominator0 * denominator1
 
if user_answer == new_denominator:
	print("Great, I calculated",new_denominator,"as well.  Good math skills!")
else: 
	print("I got a different answer.  Please recalculate your answer.")
	user_answer = int(input("What did you calculate for the numerator this time?")
	if user_answer == new_denominator:
		print("Great, I calculated",new_denominator,"as well.  Good math skills!")
	else: 
		print("Something seems to be wrong.  It might be necessary to rerstart this program.")
		exit()
time.sleep(2)

# Print the new fraction. 
print("The new fraction is",new_numerator,"/",new_denominator,".")
print("Wasn't that easy?")
time.sleep(2)

# Dividing Fractions Starts Here 
print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")

