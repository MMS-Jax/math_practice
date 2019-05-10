# Carson S., Multiply and Divide Fractions, 05/06/2019 Ver 0.9

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
print("To multiply two fractions, you must keep the first fraction the same, and then multiply the first fraction by the reciprocal of the second fraction. \n")
dnumerator0 = int(input("Type the first numerator and press ENTER \n"))
ddenominator0 = int(input("Type the first denominator and press ENTER \n"))
print("The first fraction is" , dnumerator0 , "/" , dnumerator0 , "\n")
dnumerator1 = int(input("Type the second numerator and press ENTER \n"))
ddenominator1 = int(input("Type the second denominator and press ENTER \n"))
print("The second fraction is" , dnumerator1 , "/" , ddenominator1 ,"\n")
new_dnumerator = dnumerator0 * dnumerator1
new_ddenominator = ddenominator1 * ddenominator0
print("The new fraction is" , new_dnumerator , "/" , new_ddenominator , "\n")
decimal_dversion = new_dnumerator/new_ddenominator
print("The decimal version of that is" , decimal_dversion , "\n")