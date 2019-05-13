# Shruthi Manikandan, Multiply and Divide Fractions, 05/06/19, version 0.4

print("Welcome to my program! Would you like to see a magic trick involving fractions?\n")
user_name = input("What shall I refer to you as? (Type it in and press enter)\n")
print("Henlo,", user_name, "how was your day?\n")

print("This program requires the numerators and denominators for both fractions.\n")

# Variables for Fraction 0.
numerator0 = 0
denominator0 = 0
print("The first fraction is", numerator0, "/", denominator0, ".\n")

# Variables for Fraction 1.
numerator1 = 0
denominator1 = 0
print("The second fraction is", numerator1, "/", denominator1, ".\n")

print("When multiplying fractions, you multiply the numerators together.\n")
print("Then you multiply the denominators together.\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator, "/", new_denominator, ".\n")
print("Now you can try!\n")

numerator0 = int(input("Type in the first numerator's value.\n"))
numerator1 = int(input("Type in the second numerator's value.\n"))

denominator0 = int(input("Type in the first denominator's value.\n"))
denominator1 = int(input("Type in the second denominator's value.\n"))

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator, "/", new_denominator, ".\n")

