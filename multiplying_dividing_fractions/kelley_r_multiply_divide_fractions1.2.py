# Ryan K., Multiplying and Dividing Fractions, 05/06/2019 

#Numerators
numerator1 = 3
numerator2 = 7
#Denominators
denominator1 = 6
denominator2 = 28
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
print("To divide fractions, you have to multiply the 1st numerator (3) by the 2nd denominator (28), and the 1st denominator (6) by the 2nd numerator (7)")
print("This gives you", Num3D, "/", Den3D,"or", FracDiv, ".\n")
#PrintMultFrac
print("Fraction 1 multiplied by fraction 2 is", FracProduct,"or", Num3P,"/", Den3P,)
#ExplainMultFrac
print("To multiply fractions, you have to multiple the 1st numerator (3), by the 2nd numerator (7), and the 1st denominator (6), by the 2nd denominator (28)")
print("This gives you", Num3P, "/", Den3P,"or", FracProduct, ".\n")