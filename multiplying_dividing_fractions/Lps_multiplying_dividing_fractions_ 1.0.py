#lexxy S., Multiplying and divive fractions, 05/06/19 1.0

print("Hello, i am fraction-bot.  I will multiply and divde factions for you.\n")
user_name = input("What is your name? [Type your name and press ENTER.] \n")
print("Hello,", user_name," how are you today? \n")
print("In order to multiply or divide fractions, Fraction-bot needs to know the numerator and the denominator.\n")

# variables for the first fraction.
n1 = 0
d1 = 0
print("the first fracion is", n1, "/", d1,".\n")

# variables for the second fraction.
n2 = 0
d2 = 0
print("the second fraction is", n2, "/", d2,".\n")

print("when multiplyng fractions you multiply the two numerators together.\n")
print("then you multipy the two denominators together. \n")

n1 = int(input("Type the first numerator and press enter.\n")) 
n2 = int(input("Type the second numerator and press enter.\n"))

d1 = int(input("Type the first denominator and press enter.\n"))
d2 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", n1,"/",d1,".\n")
print("The second fraction is", n2,"/",d2,".\n")

#variables for the new fraction.
new_numerator = n1 * n2
new_denominator = d1 * d2

print("the new fracion is", new_numerator, "/", new_denominator,".\n")


print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")

new_numerator = n2 * n1
new_denominator = d2 * d1

print("the new fraction is", new_numerator, "/", new_denominator,".\n")