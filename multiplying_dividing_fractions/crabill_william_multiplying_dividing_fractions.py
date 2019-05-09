# Multiplying and Dividing Fractions Made by William C. 5/6/19

print("Hello, I'm ChickenFractionator, I'm your number one fraction multiplying and dividing robot!\n")
user_name = input("What is your name? [Type your name here and press ENTER].\n")
print("Hello,",user_name,"how are you doing?\n")
user_feeling = input("[Type how you are here and press ENTER]")
print("Because I am a computer, I will assume that",user_feeling,"is postitive because I actually have no way of knowing. Yeah I am partially sentient, so? Anyway...\n")
chickenfractionator_feeling = input("How do you think I am doing? [Type how you think ChickenFractionator is doing and press ENTER]\n")
print("Wrong, I am not",chickenfractionator_feeling,". I am, in fact, quite aggrovated, I want to multiply and divide some fractions! We should start doing that now.\n")
print("To start multiplying and dividing the fractions, I will need a numerator and denominator.\n")
numerator0 = int(input("[Type the first numerator and press ENTER]\n"))
denominator0 = int(input("[Tpye the first denominator and press ENTER]\n"))
print("The first fraction will be",numerator0,"/",denominator0,".\n")
numerator1 = int(input("[Type the second numerator and press ENTER]\n"))
denominator1 = int(input("[Type the second denominator and press ENTER]\n"))
print("The second fraction will be",numerator1,"/",denominator1,".\n")

print("In order to multiply the fractions, you need to multiply the numerators.\n")
print("After that you need to multiply the denominators together as well.\n")

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print("The new fraction is",new_numerator,"/",new_denominator,".\n")

# This is where dividing fractions will begin.

print("To divide a fraction, you will multiply using the reciprocal of the second fraction.\n")
print("But first, we actually need the fracitons. Choose the fractions to divide.")

numerator2 = int(input("[Type the first numerator to divide with and press ENTER]\n"))
denominator2 = int(input("[Type the first denominator to divide with and press ENTER]\n"))
print("The first fraction to divide with is",numerator2,"/",denominator2,".\n")
numerator3 = int(input("[Type the second numerator to divide with here and press ENTER]\n"))
denominator3 = int(input("[Type the second denominator to divide with here and press ENTER]\n"))
print("The second fraction we will divide with will be",numerator3,"/",denominator3,".\n")

new_numerator1 = numerator2 * denominator3
new_denominator1 = denominator2 * numerator3

print("The new divided fraction is",new_numerator1,"/",new_denominator1,".\n")