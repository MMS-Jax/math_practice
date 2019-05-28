# Benjamin Hadziabdic, Multiplying and Dividing Fractions, 05/20/2019, Version 0.8

print('This is a program about multiplying and dividing fractions for you because you are too lazy to.\n')
user_name = input('What do you want me to call you? [Type your potentially fake name and press ENTER].\n')
print('Wassup broski.',user_name,'...kinda generic but whatever\n')

print('I assume you know what a fraction is. Tell me what the two numerators and denominators. If you dont know what a fraction is, hit ALT+F4.\n')


print('When multiplying fractions, you multiply the numerator by the other numerator\n')
print('Same thing with the denominator.\n')

numerator0 = int(input('and the first numerator is...? type your number and hit ENTER\n'))
numerator1 = int(input('and the second numerator is...? type your number and hit ENTER\n'))

denominator0 = int(input('and the first denominator is...? type your number and hit ENTER\n'))
denominator1 = int(input('and the second denominator is...? type your number and hit ENTER\n'))

print('Aight, BET.', numerator0,'/', denominator0,'.\n')
print('Okay I see you.', numerator1,'/', denominator1,'.\n')

new_numerator = numerator0 * numerator1
new_denominator = denominator0 * denominator1

print('Okay I see you MORE.', new_numerator,'/', new_denominator,'.\n')

# This is where division starts.

print('To divide a fraction, you will multiply using the reciprocal or inverse of the second fraction.\n')

numerator0 = int(input('and the first numerator is...? type your number and hit ENTER\n'))
numerator1 = int(input('and the second numerator is...? type your number and hit ENTER\n'))

denominator0 = int(input('and the first denominator is...? type your number and hit ENTER\n'))
denominator1 = int(input('and the second denominator is...? type your number and hit ENTER\n'))

print('This again eh?.', numerator0,'/', denominator0,'.\n')
print('Epic.', numerator1,'/', denominator1,'.\n')

new_numerator = numerator0 * denominator1
new_denominator = denominator0 * numerator0

print('Okay I see you as much as humanly possible.', new_numerator,'/', new_denominator,'.\n')