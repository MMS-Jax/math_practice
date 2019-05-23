# Joseph., Multiplying and Dividing Fraction, 05/06/19, version 0.9

print("Hi, my fish is drowning please help me solve a math question to revive him. \n")
user_name = input("Whats your name? [Type your name and press ENTER.]\n") 
print("Hello, ", user_name,"how are you today?")

print("For this program, i need to know the numerator and denominator for both fractions.\n")


numerator0 = 0
denominator0 = 0
print("the first fraction is",numerator0,"/",denominator0,".\n")

numerator1 = 0
denominator1 = 0
print("the second fraction is",numerator1,"/", denominator1,".\n" )

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
denominator0 = int(input("Type the first denominator and press enter.\n"))

numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1  
new_denominator = denominator0 * denominator1 

print("The new fraction is", new_numerator,"/",new_denominator,".\n"). 

print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")
