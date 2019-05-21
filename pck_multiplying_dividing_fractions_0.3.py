# Parker K., Multiplying And Dividing Fractions, 05/06/19

print("Hello my name is fractiony boy. I can multiply and divide fractions for you.\n")
user_name = input("What is your name? [Type your name and press ENTER.]\n")
print("Hello,", user_name, "how are you today?\n")

print("For this program, I need to know the numerator and denominator for both the fractions.\n")

# Variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0,"/",denominator0,".\n")

# Variables for fraction 1.
numerator1 = 0
denominator1 = 0
print("The first fraction is", numerator1,"/",denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

# Input the first fraction. 
numerator0 = int(input("Type the first numerator and press enter.\n")) 
denominator0 = int(input("Type the first denominator and press enter.\n"))

# Input the second fraction. 
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1 # Multiply the two numerators together. 
new_denominator = denominator0 * denominator1 # Multiply the two denominators together.

print("The new fraction is", new_numerator,"/",new_denominator,".\n") # Print the new fraction on the screen.

new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1