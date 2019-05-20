#isabella S. , multiplying and dividing fractions 05/06/2019 version 1.0

print("hello! my name is super math bot i will multiply and divide fractions for you!\n")
user_name = input("what is your name? [Type your name and press ENTER.]\n")
print("Hello,",user_name,"how are you today?")

print("for this program, i need to know the numerator and denominator for each fraction.\n")

#variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("the first fraction is", numerator0,"/",denominator0,".\n")

# variables for fraction 1.
numerator1 = 0
denominator1 = 0
print("the seconed fraction is", numerator1,"/",denominator1,".\n")

print("when multipliying fractions you will miltiply the two numerators together\n")
print("then you will multiply the two denomenators together\n")

numerator0 =  int(input("Type the first numerator and press enter.\n")) 
numerator1 =  int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("the new fraction is", new_numerator,"/",new_denominator,".\n")

#this is where the division of the fractions will start.

print("to divide a fraction, you will multiply using the reciprocal or inverse of the seconed fraction.\n")

#variables for fraction 0.
numerator0 = 0
denominator0 = 0
print("the first fraction is", numerator0,"/",denominator0,".\n")

print("now you will multipltiply the fraction by it's reciprical\n")

#variables for fraction 0.
numerator1 = 0
denominator1 = 0
print("the seconed fraction is", numerator0,"/",denominator0,".\n")

numerator0 =  int(input("Type the first numerator and press enter.\n")) 
numerator1 =  int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1

print("the new fraction is", new_numerator,"/",new_denominator,".\n")


