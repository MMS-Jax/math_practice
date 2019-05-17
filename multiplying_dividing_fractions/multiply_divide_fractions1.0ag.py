# Adding And Subtracting Fractions 5/06/19 Avrielle G. 

print("welcome to Math-Ro-Bot I can multiply and divide fractions for you!\n")
user_name = input("What's your name? [Type your name and press ENTER.]\n")
print("Hello", user_name, "How is your day going?\n")

print("For this area, I need to know the numerator and the denoinator so i can multiply or divide them.\n")

# variables for multiplying and dividing 0
numerator0 = 0
denominator0 = 0

print("The first fractions is", numerator0,"/",denominator0,".\n")

# variables for multiplying and dividing 1
numerator1 = 0
denominator1 = 0
print("The second fraction is", numerator1,"/",denominator1,".\n")

print("When adding fractions you add the two numbers together.\n")                                                                                                                                 

numerator0 = int(input("Type the first numerator and press enter .\n"))
denominator0 = int(input("Type the first denominator and press enter .\n"))


numerator0 = int(input("Type the second numerator and press enter .\n"))
numerator1 = int(input("Type the second denominaor and press enter .\n"))


#This is where the dividing of the fraction beggings
new_numerator = numerator0 * denominator1
new_denominator = numerator1 * denominator0

print("The new fraction is", new_numerator,"/",new_denominator,".\n")

print("We got this number by fliping the second set of numerator and denominator .\n")

print("FOR EXAMPLE we have 5/6 divided by 7/8 we would flip the 7/8 to get 8/7 .\n")

print("Restart the program to do it again! .\n")