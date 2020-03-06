# Slope-Intercept Equation Solver
import time 
print("This program will solve equations for slope-intercept that use y = mx + b format.")

print("The first thing I want to know is the y-intercept, which is represented as b.")
b = int(input("What is the y-intercept?  Type the number and press enter."))

print("The next thing I need to know is the slope, which is represented as m.")
print("If the slope is given as a fraction, we need to convert it to a decimal first.")
is_slope_fraction = int(input("Is the slope a fraction?  Type 0 for no, type 1 for yes.  Then press enter."))

if is_slope_fraction == 0:
    m = int(input("Please enter the slope as a whole number then press enter."))
    print("The slope is",m,".")
    time.sleep(5)
elif is_slope_fraction == 1: 
    numerator = int(input("Please enter NUMERATOR (top number) of the slope."))
    denominator = int(input("Please enter the DENOMINATOR (bottom number) of the slope."))
    m = (numerator / denominator)
    print("The slope is",m,".")
    time.sleep(5)
else:
    print("You have done something wrong. I am going to exit.  Please restart.")
    time.sleep(5)
    exit()

print("Ok, now I have the slope and the y-intercept.  I can start solving equations here shortly.")

x = int(input("Please type an integer value for x then press enter."))

loop_count = 0
num_coords = int(input("How many cooridnate pairs would you like me to calculate?"))
                 
print("The coordinate pairs in (x,y) format are as follows:")
while loop_count < num_coords:
    y = ((m*x) + b)
    print(x,",",y)
    x += 1
    loop_count += 1


    
