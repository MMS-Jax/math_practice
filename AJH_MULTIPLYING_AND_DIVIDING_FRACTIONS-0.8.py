#AARON_HUNGERMAN, MULTIPLY AND DIVIDE FRACTIONS, 5-6-19, 1.0

print("YO! WUT IZZZzzz UP. IMA GONNA DO UR MATH CUZZZzzz ima DR. Savage FractionZZZzzz!!!!!!!!!!!!!!!!!!!!!!!!!!!\n")
print("to do the multipying and dividing of fractions savgely we must know blank and blank about them")
user_name = input("what izzzz your name? [type your name and press enter]\n")
print("Wussup",user_name,"How are you today?")

print("For this savage program i need to know the numerator and denominator for both fractions.\n")

#variables for fraction0
numerator0 = 0
denominator0 = 0
print("The first savage fraction is", numerator0, "/",denominator0,".\n")

#variables for fraction 1
numerator1 = 0
denominator1 = 0
print("The second savage fraction is", numerator1, "/",denominator1,".\n")

print("When multiplying savage fractions you multiply the two numerators together. \n")
print("Then you must multiply the denominators. \n")
#input first fraction
numerator0 = int(input("type the first numerator and press enter. \n"))
denominator0 = int(input("type the first denominator and press enter. \n"))

# Input the second fraction. 
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1
print("The new savage fraction is" , new_numerator, "/" , new_denominator, ". \n")

#dis iz where division will start
print("To divide a fraction, you will multiply using the reciprical or inverse of the second fraction. \n")

new_numerator1 = denominator0 * numerator1
new_denominator1 = numerator0 * denominator1
print("The new savage fraction is" , new_numerator1, "/" , new_denominator1, ". \n")