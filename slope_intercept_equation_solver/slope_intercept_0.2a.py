# Slope-Intercept Equation Solver by Ryan Kelley, Version 0.2, March 05, 2020
import time 
print("This program will solve equations for slope-intercept that use y = mx + b format.\n")
time.sleep(3)
print("The first thing I want to know is the y-intercept, which is represented as the variable: b.\n")
time.sleep(3)
print("The y-intercept indicates where a line intercepts, or crosses, the y-axis on a coordinate plane.\n")
time.sleep(3)
b = int(input("What is the y-intercept?  Type the number and press enter.  It should be an integer.  "))
print("The y-intercept you entered was:",b,".\n")
time.sleep(3)
print("The next thing I need to know is the slope, which is represented as the variable: m.\n")
time.sleep(3)
print("Slope is often referred to as rise-over-run.\n")
time.sleep(3)
print("It indicates how far up or down the line will move on the y-axis for each point on the x-axis.\n")
time.sleep(3)
print("If the slope is given as a fraction, we need to convert it to a decimal first.\n")
is_slope_fraction = int(input("Is the slope a fraction?  Type 0 for no, type 1 for yes.  Then press enter.  "))

if is_slope_fraction == 0:
    m = int(input("Please enter the slope as a whole number then press enter.  "))
    print("The slope is",m,".\n")
    time.sleep(3)
elif is_slope_fraction == 1: 
    numerator = int(input("Please enter NUMERATOR (top number) of the slope.  "))
    denominator = int(input("Please enter the DENOMINATOR (bottom number) of the slope.  "))
    m = (numerator / denominator)
    print("The slope is",m,".\n")
    time.sleep(3)
else:
    print("Please enter 0 if the slope is an integer and 1 if it is a fraction. I am going to exit the program.  Please restart it.\n")
    time.sleep(3)
    exit()
time.sleep(3)
print("Ok, now I have the slope and the y-intercept.  I can start solving equations here shortly.\n")
time.sleep(3)
print("You need at least two coordinate pairs to correctly graph a line on a coordinate plane.\n")
time.sleep(3)
num_coords = int(input("How many pairs of coordinates do you want?  Type an integer and press enter.  "))
loop_count = 0

while loop_count < num_coords:
    x = int(input("Please enter an integer value for x.  "))
    print("Ok, the y-intercept is ",b,"and the slope is ",m,".  Let me solve for y now...\n")
    time.sleep(3)
    y = round(((m*x) + b))
    print("The coordinates are (",x,"),(",y,").\n")
    time.sleep(3)
    loop_count += 1

print("You can use these coordinates to plot a line on a coordinate plane now.\n")
time.sleep(3)
print("I hope you have found this program useful.\n")
time.sleep(3)
print("I will now exit.  Please restart me if you need to solve another equation.\n")
time.sleep(3)
exit() 


    
