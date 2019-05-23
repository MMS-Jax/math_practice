# joshua_edwards,multiply and divide fractions 05/06/2019 1.0

print("hello,my name is fraction bot i can do any fraction math problem for you i am the smarted bot in the world!!!!!!!!!!!!\n")
user_name = input("what is your  [type your name and press ENTER.]\n")
print ("hello ," ,user_name, "how are you today?")

print("for this program ,. I need to know the numerator and the denomenator for both fractions.\n")

#variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("the first fraction is",numerator0,"/",denominator0,".\n" )
#variables for fraction 1.
numerator1 = 0
denominator1 = 0

print("the second fraction is",numerator1,"/",denominator1,".\n" )

print("when multipliying fractions you multiply the two nemerators together.\n ")
print("then you will multipy the two denomernators togethors.\n ")
#input the first fraction
numerator1 = int(input("Type the first numerator and press enter.\n"))
denominator1 = int(input("Type the first denominator and press enter.\n"))

# Input the second fraction. 
numerator0 = int(input("Type the second numerator and press enter.\n"))
denominator0 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1 # Multiply the two numerators together. 
new_denominator = denominator0 * denominator1 # Multiply the two denominators together.

print("the new fraction is",new_numerator,"/",new_denominator,".\n" )


print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")

user_name = input("what is your  [type your name and press ENTER.]\n")
print ("hello ," ,user_name, "how are you today?")

print("for this program we need to Turn the second fraction (the one you want to divide by) upside down (this is now a reciprocal)..\n")

print("Step 2. Multiply the first fraction by that reciprocal.\n")

print("Step 3. Simplify the fraction (if needed).\n")

#variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("the first fraction is",numerator0,"/",denominator0,".\n" )
#variables for fraction 1.
numerator1 = 0
denominator1 = 0
# input the first fraction
print("the second fraction is",numerator1,"/",denominator1,".\n" )
numerator1 = int(input("Type the first numerator and press enter.\n"))
denominator1 = int(input("Type the first denominator and press enter.\n"))

# Input the second fraction. 
numerator1 = int(input("Type the second numerator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))


new_numerator = numerator0 * denominator1 # multiply the oposite denomonator from numerator 

new_denominator = numerator1 * denominator0 # multiply the oposite numurator from denomonator 

print("the new fraction is",new_numerator,"/",new_denominator,".\n" )