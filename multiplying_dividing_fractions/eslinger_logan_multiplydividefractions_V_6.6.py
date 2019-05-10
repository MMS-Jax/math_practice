# Multiplying/Dividing Fraction Calculator by Logan E. | Version 6.6 

# Welcome username screen insert here.
user_name = input("Hi there, what is your name?[Type your name and press enter]\n")

print("Welcome", user_name,".\n")

#Yes/No Input Here
answer = input("Are you ready to start calculating?").upper()
if answer == "YES":
   print("All right lets start!")
elif answer == "NO":
   print("Okay, you can exit the program now.")

import time
time.sleep(2)  # Delay for 2 seconds

print("To start multiplying and dividing, I need to know the numerator and the denominator.\n")

# Variables for fraction 0
numerator0 = int(input("Type the first numerator here:\n"))
denominator0 = int(input("Type the first denominator here:\n"))

import time
time.sleep(1.5)  # Delay for 2 seconds

print("The first fraction is", numerator0,"/",denominator0,".\n")

# Variables for fraction 1
numerator1 = int(input("Type the second numerator here:\n"))
denominator1 = int(input("Type the second denominator here:\n"))

import time
time.sleep(1.5)  # Delay for 2 seconds

print("The second fraction is", numerator1,"/",denominator1,".\n")

import time
time.sleep(1.5)  # Delay for 2 seconds

print("When multiplying fractions, you multiply the two numerators together.\n")

import time
time.sleep(1.5)  # Delay for 2 seconds

print("After this you will multiply the two denominators together.\n")

import time
time.sleep(1.5)  # Delay for 2 seconds

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")

import time
time.sleep(1.5)  # Delay for 2 seconds

# This is where the division of fractions will start.

print("To divide fractions, you will multiply using the reciprocal or inverse of the second fraction.\n")

import time
time.sleep(2.5)  # Delay for 2 seconds

new_numerator1 = numerator0 * denominator1
new_denominator1 = denominator0 * numerator1

print("The new divided fraction is", new_numerator1,"/",new_denominator1,".\n" )

import time
time.sleep(2)  # Delay end v 1.2 for 2 seconds

print("Thank you for using my multiplying and dividing fraction calculator.")

#Yes/No Input Here V.E.1
answer = input("Did you enjoy this calculator?").upper()
if answer == "YES":
   print("Thanks! Have a good rest of your day!")
elif answer == "NO":
   print("I'm sorry, but thank you for trying this anyway.")