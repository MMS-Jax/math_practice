# Ryan K., Slope-Intercept Ordered Pair Solver, 05/14/2019, v0.0
import time # Imports a LIBRARY of methods related to time. 

print("This program will solve slope-intercept equations in the form of y = mx + b.\n")
print("m represents the slope of the line.  b represents the y-intercept of the line.\n")
print("After inputting a value for x, this program will solve for y.  Then five ordered pairs will be calculated and printed to the screen.\n")
time.sleep(10) # This is a METHOD that pauses the program for the number of seconds indicated.  Make this code pause for three seconds.  

# The first thing your code must do is determine whether the SLOPE is given as a whole number or a fraction.  

# If it is a WHOLE NUMBER, you can save the value as an int to a variable called m or slope. 
# If it is a FRACTION, you will need to convert it to a float using DIVISION then save the value to a variable called m. 

if : # You need to figure out the code needed here if the slope is a whole number. 
    # Execute this code if the slope is a whole number. 
    # Have the user input() an integer value for the slope and save it to the variable m.
    # Make sure to print() the slope back to the screen so the user knows it is correct. 
else:  
    # Execute the code in this block if the slope is a fraction. 
    # You will need to know the NUMERATOR and DENOMINATOR for the slope.  
    # You must use divison, which is the / character, to convert from a fraction to a decimal.  
    # Make sure to print() the slope back to the screen so the user knows it is correct. 

# Pause the program for five seconds here so the user can read the information. 


# Next you need the user to input() the y-intercept of the equation which is represented by the variable b. 
# Make sure to print() the y-intercept back to the screen. 
# Pause the program for five seconds here so the user can read the information. 


# After you have the y-intercept you need the user to enter a starting value for x. 
# You will need to use input() and store the value as an int to the variable called x. 
# Make sure to print the variable back to the screen so the user knows it is correct. 
# Pause the program for five seconds here so the user can read the information. 


while : # Make this loop run 5 times. 
    y = ((m * x) + b) # This will solve for y using the slope, y-intercept, and x values entered earlier. 
    print("The ordered pair is (",x,",",y,").\n")  # This will print the ordered pair to the screen using (x, y) form.
    # Increment / decrement x by 1 each time through the loop. 
    # Increase your loop control variable by 1.  



