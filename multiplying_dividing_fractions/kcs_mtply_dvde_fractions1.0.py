# Carson S., Multiply and Divide Fractions, 05/06/2019 Ver 1.0

print("Hello, my name is MathHomeworkBotwork. My Master sent me to help you with your math.  I can MULTIPLY and DIVIDE FRACTIOMANIANS for you, or on your planet, they call them fractions. \n")
user_name = input("What is your name? Type your name and press enter to continue. \n")
print("Nice to meet you,", user_name , "\n")

print("MathHomeworkBotwork OVERLOAD: REBOOT \n")
print("Okay, I am better now. \n")
print("For this program, I will need a numerator and denominator for both numbers.")

# Variables for fraction 0.
numerator0 = int(input("Type the first numerator and press ENTER. \n"))
denominator0 = int(input("Type the first denominator and press ENTER. \n"))
print("The first fraction is", numerator0 , "/" , denominator0 ,"\n")
# Variables for fraction 1.
numerator1 = int(input("Type the second numerator and press ENTER. \n"))
denominator1 = int(input("Type the second denominator and press ENTER. \n"))
print("The second fraction is", numerator1 , "/" , denominator1 ,'.\n')
print("When multiplying two fractions you multiply the two numerators together. \n")
print('Then you will multiply the denominators together too. \n')
new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1
print("The new fraction is" , new_numerator , "/" , new_denominator , "\n")
decimal_version = new_numerator / new_denominator
print("The decimal version of that is" , decimal_version , "\n")
# Division Starts Here.
print("To divide two fractions, you must keep the first fraction the same, and then multiply the first fraction by the reciprocal of the second fraction. \n")
div_numerator0 = int(input("Type the first numerator and press ENTER \n"))
div_denominator0 = int(input("Type the first denominator and press ENTER \n"))
print("The first fraction is" , div_numerator0 , "/" , div_denominator0 , "\n")
div_numerator1 = int(input("Type the second numerator and press ENTER \n"))
div_denominator1 = int(input("Type the second denominator and press ENTER \n"))
print("The second fraction is" , div_numerator1 , "/" , div_denominator1 ,"\n")
new_div_numerator = div_numerator0 * div_denominator1
new_div_denominator = div_denominator0 * div_numerator1
print("The new fraction is" , new_div_numerator , "/" , new_div_denominator , "\n")
decimal_dversion = new_div_numerator/new_div_denominator
print("The decimal version of that is" , decimal_dversion , "\n")