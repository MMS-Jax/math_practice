# Ryan K., Slope-Intercept Ordered Pair Solver, 05/10/2019, v0.1

print("This program will solve slope-intercept equations in the form of y = mx + b.\n")
print("m represents the slope of the line.  b represents the [REPLACE] of the line.\n")
print("After inputting a value for x, this program will solve for y.  Then five ordered pairs will be calculated and printed to the screen.\n")



whole_or_fraction = int(input("Is the slope a whole number or a fraction?  Enter 0 for a whole number.  Enter 1 for a fraction.\n"))

if whole_or_fraction == 0: # == translates to "is this equal to" which is different than = which means "make this equal to".
    m = 0 # Makes the slope an int data type. 
    print("Ok, the slope will be stored as an integer.\n")
    m = input("What is the slope?  [Type a number and press ENTER.]\n")
    print("The slope entered is:", m)
else: 
    numerator = int(input("What is the numerator of the slope?\n"))
    denominator = int(input("What is the denominator of the slope?\n"))
    m = numerator / denominator # Calculates the slope with division. 
    print("The slope entered is:", m) # Can you figure out how to print just two decimal places?


