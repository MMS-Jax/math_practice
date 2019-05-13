# Kailey D., Multiplying and Dividing Fractions, 05/06/2019, version 0.6

print("Hello! My name is FattoCattoPugFraction and I will multiply and Divide Fractions for you.\n")
user_name = input("What is your name? [ Type your name and press ENTER.]\n")
print("Hello, ", user_name," how are you today?\n")

print("In order to find the answer, you need to know the numerator and the denominator for both fractions.\n")

# Variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("The fisrt fraction is ", numerator0, "/",denominator0,".\n")

# Variables for fraction 1.
numerator1 = 0
denominator1 = 0
print("The second fraction is ", numerator1, "/",denominator1,".\n")

print("Whenever you multiply fractions you multiply the two numerators together.\n")
print("Next you are going to multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator then press enter.\n"))
numerator1 = int(input("Type the second numerator then press enter.\n"))

denominator0 = int(input("Type the first denominator then press enter.\n"))
denominator1 = int(input("Type the second denominator then press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("Your new fraction is", new_numerator,"/", new_denominator,".\n")

# this is where the division of the fractions will start.
pie = 22 / 7
print(pie)
print("In order to divide a fraction, you will multiply using the inverse of the second fraction.\n")