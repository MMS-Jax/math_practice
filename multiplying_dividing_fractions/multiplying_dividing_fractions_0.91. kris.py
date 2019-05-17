# kris m, mulitiplying and dividing fractions 05/09/2019 virsion 0.9

print("Hello,  I can multiply and divide fractions for you so you can get good grades in math class!\n")

user_name = input("What is your name? [Type your name and press ENTER.]\n")

print("Hello,", user_name,"how was your day?\n")

print("for me to help you get good grades i will need your numerator and the denominator for both of your fractions.\n")

numerator0 = 0
denominator0 = 0

print("The first fraction is", numerator0,"/",denominator0,".\n")


numerator1 = 0
denominator1 = 0

print("The second fraction is", numerator1,"/",denominator1,".\n")

print("When multiplying fractions you multiply the two numerators together.\n")

print("Then you will multiply the two denominators together.\n")

# first fraction. 
numerator0 = int(input("Type the first numerator and press enter.\n")) 

denominator0 = int(input("Type the first denominator and press enter.\n"))

# second fraction. 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")

print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1  
new_denominator = denominator0 * denominator1 

print("The new fraction is", new_numerator,"/",new_denominator,".\n") 

print("To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n")

print("hope this helped you get thoses good grades you came here for!\n")