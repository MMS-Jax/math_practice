# Jackson C., Multpily and dividing fractions, 05/06/19 version 0.5

print("hello my name is Big Billy Chilly Boi and I multiply and divide fractions\n")
print("To multiply and divide fractions for you master, I need to know the numerator and denominator.\n")
user_name = input("Hello what is your name? [enter your name here and then press enter\n")
print("Hello, " , user_name," how are you today?\n")

print("For this program, I need to know the numerator and denominator for both fractions.\n")

print("When multiplying fractions you multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n")

numerator0 = int(input("Type the first numerator and press enter.\n")) 
numerator1 = int(input("Type the second numerator and press enter.\n"))

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is" , numerator0 , "/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 = numerator1
new_denominator = denominator0 = denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")