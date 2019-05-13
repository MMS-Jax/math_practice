# Ryan K., Multiplying and Dividing Fractions, 05/06/2019 
#Introduction
print("Hi! My name is NoobMaster69!")
Username = input("What is your name? [Type Your Name, and then type ENTER]\n")
print("Hello", Username,"! How are you?")
print("Today, I will teach you how to multiply and divide fractions!")
#Numerators
numerator1 = int(input("Type a Number to be your 1st numerator, then hit Enter\n"))
numerator2 = int(input("Type a Number to be your 2nd numerator, then hit Enter\n"))
#Denominators
denominator1 = int(input("Type a Number to be your 1st denominator, then hit Enter\n"))
denominator2 = int(input("Type a Number to be your 2nd denominator, then hit Enter\n"))
#fractions
fraction1 = numerator1 / denominator1
fraction2 = numerator2 / denominator2
#PrintFractions
print("Fraction 1 is", numerator1,"/", denominator1,",")
print("Fraction 2 is", numerator2,"/", denominator2,",\n")
#Num3
Num3P = numerator1 * numerator2
Num3D = numerator1 * denominator2
#Den3
Den3P = denominator1 * denominator2
Den3D = denominator1 * numerator2
#MultFractions
FracProduct = fraction1 * fraction2
#DivFractions
FracDiv = fraction1 / fraction2
#PrintDivFrac
print("Fraction 1 divided by fraction 2 is", FracDiv,"or", Num3D, "/", Den3D,)
#ExplainDivFrac
print("To divide fractions, you have to multiply the 1st numerator (", numerator1, ") by the 2nd denominator (",denominator2, "), and the 1st denominator (",denominator1, ") by the 2nd numerator (", numerator2, ")")
print("This gives you", Num3D, "/", Den3D,"or", FracDiv, ".\n")
#PrintMultFrac
print("Fraction 1 multiplied by fraction 2 is", FracProduct,"or", Num3P,"/", Den3P,)
#ExplainMultFrac
print("To multiply fractions, you have to multiple the 1st numerator (",numerator1, "), by the 2nd numerator (",numerator2, "), and the 1st denominator (",denominator1, "), by the 2nd denominator (",denominator2,")")
print("This gives you", Num3P, "/", Den3P,"or", FracProduct, ".\n")
#Conclusion
print("Thank you for joining me today! I hope to see you again, Goodbye!")