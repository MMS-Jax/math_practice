# Josephine Y. multiplying and dividing fractions, 05/06/19 0.7

print ("Hello! My name is Barry B. Benson and i will help you muliply and divide fractions.\n")
print('In order to muliply or divide fractions you will need to input your numerator and denominator')

user_name = input ('What is your name? [type in your name and press ENTER] \n')
print("Hello", user_name, "How are you today?") 

print("For this program, I need to know the numerator and denominator for both fractions.\n")

# Variables for fraction 0
numerator_0 = input ("What is the numerator for the first fraction? \n")
denominator_0 = input ("What is the numerator for the first fraction? \n")
print("The first fraction is", numerator_0 , "/", denominator_0 , ".\n")

# Variables for fraction 1
numerator_1 = input ("What is the numerator for the second fraction? \n")
denominator_1 = input ("What is your denominator for the second fraction? \n")
print("The second fraction is", numerator_1 , "/", denominator_1 , ".\n")

print("When mulitplying fractions you muliply the two numerators together. \n")
print("Then you will multiply the two denominators together. \n")

new_numerator = numerator_0 * numerator_1
new_denominator = denominator_0 * denominator_1

#This is where the divisions of fractions will start.

print("The new fraction is", new_numerator, "/", new_denominator, ".\n")
# Variables for fraction 0
numerator_2 = input ("What is the numerator for the first fraction? \n")
denominator_2 = input ("What is denominator for the first fraction? \n")

print("The first fraction is", numerator_2, "/", denominator_2, ".\n")

# Variables for fraction 1
numerator_3 = input ("What is the numerator for the first fraction? \n")
denominator_3 = input ("What is the denominator for the second fraction? \n")
print("The second fraction is", numerator_3, "/", denominator_3, ".\n")

print('To divide a fraction, you will multiply using the reciprical or inverse of the second fraction. \n')

new_numerator = numerator_2 * denominator_3
new_denominator = denominator_2 *  numerator_3