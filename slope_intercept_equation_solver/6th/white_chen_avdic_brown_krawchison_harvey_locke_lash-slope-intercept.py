# Ryan Kelley, March 06, 2:54PM, Slope-Intercept Equation Solver

print("This program will allow us to solve slope-intercept equations.")

print("In the slope-intercept equation form m is the slope and b is the y-intercept.")

m = int(input("Please type the slope of the line and press enter."))
print(m) 

b = int(input("Please type the y-intercept of the line and press enter."))
print(b)

num_coords = int(input("How many pairs of coordinates do you want?"))

loop_count = 0

while loop_count < num_coords:
    x = int(input("Please enter an integer value for x.  "))
    y = (m * x) + b
    print(x,y)
    loop_count += 1
    
