#Evan L. fraction robot 5/6/19

print("Give me fractions to multiply, if you dare.\n")
print("if you are up to the challenge you must give me the numerator and denominator for each desired fraction.")

numerator0 = int(input("What is the first numerator? [Type number and press enter.]"))
denominator0 = int(input("What is the first denominator? [Type number and press enter.]"))
print("Then your first fraction must be",numerator0,"/",denominator0,".")

numerator1 = int(input("What is the second numerator? [Type number and press enter.]"))
denominator1 = int(input("What is the second denominator?[Type number and press enter.]"))
print("Then your second fraction must be",numerator1,"/",denominator1,".")

#where mutiplying/dividing happens
print("To multiply these fractions enter '0' to divide them enter '1'.")
answer= input()
if answer == "0":
    new_numerator = numerator0 * numerator1
    new_denominator = denominator0 * denominator1
    print("Then your new fraction must be",new_numerator,"/",new_denominator,".")
else:
    new_numerator = numerator0 * denominator1
    new_denominator = denominator0 * numerator1
    print("Then your new fraction must be",new_numerator,"/",new_denominator,".")