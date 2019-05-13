# Klea R., Multiplying and Dividing Fractions, 05/06/19,version 0.7


print("Hello, welcome to fraction-bot 9000.  I can  multiply and divide fractions for you !\n")
user_name=input("What is your name?[Yype yuor name and press ENTER.]\n")
print("Hello,",user_name ,"How are you today?\n")

print ("For this program, i need to know the numerator and the denominator for bothe fractions.\n")

# Variables for fraction 0.
numerator0 =0
denominator0 =0
print("The first fraction is", numerator0,"/",denominator0,".")

# Variables or fraction 1
numerator1 =0
denominator1 =0
print("The first fraction is", numerator1,"/",denominator1,".")

print("When multiplying fractions you can multiply the two numerators together.\n")
print("Then you will multiply the two denominators together.\n ")

new_numerator= numerator0 * numerator1
new_denominator=denominator0 * denominator1

print("The new fracton is", new_numerator,"/", new_denominator,".")

denominator0 = int(input("Type the first denominator and press enter.\n"))
denominator1 = int(input("Type the second denominator and press enter.\n"))

print("The first fraction is", numerator0,"/",denominator0,".\n")
print("The second fraction is", numerator1,"/",denominator1,".\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is", new_numerator,"/",new_denominator,".\n")
pie = 22 / 7
print(pie)
print("To divide a fraction, you will multiply using the reciprocal or inverse of the secon")d fraction.\n