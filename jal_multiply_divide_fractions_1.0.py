#Julia L ., Multiply and Dividing Fractions version 1.0

print('Hello my name is fractionbot 900 I multiply and divide frcations.\n')
user_name = input('What is your name?\n')
print("hello,", user_name, "How are you today?\n")

print('for this program, I need to know the numerator and the denominator for both fractions.\n')

# fraction for variables 0.
numerator0 = 0
denominator0 = 0
print('The first fraction is', numerator0,'/',denominator0,'.\n')


# fraction for variable 1.
numerator1 =0
denominator1 =0

print('when multiplying fractions you multiply the two numerators together.\n')
print('Then you will multiply the two denominators together.\n')

new_numerator = numerator0 * numerator1
new_denominator = numerator0 * denominator1

denominator0 = int(input('Type the first denominator and press enter.\n'))
denominator1 = int(input('Type the second denominator and press enter.\n'))

print('The first fraction is', numerator0,'/',denominator0,'.\n')
print('The second fraction is', numerator1,'/',denominator1,'.\n')

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print('The new fraction is', new_numerator,'/',new_denominator,'.\n')

# This is where the division of the fraction will start.
pie = 22 / 7
print(pie)
print('To divide a fraction, you will multiply usint the reciprocal or inverse of the secon fraction.')
new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator1
print('The new fraction is', new_numerator,'/',new_denominator,'.\n')