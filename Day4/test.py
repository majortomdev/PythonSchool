# num1 = int(input("Enter a number:"))
# num2 = int(input("Enter another number:"))
#
#
# if num1>num2:
#     print(f"{num1} is greater than {num2}")
# elif num2>num1:
#     print(f"{num2} is greater than {num1}")
# else:
#     print(f"{num1} and {num2} are equal")

############################################

# age = 18
# has_license = True
#
#
# if age <18:
#     print("You can't drive yet. You must be 18 years old and have a license")
# elif not has_license:
#     print("You can't drive. You need to have a license")
# else:
#     print("You can drive")

#######################################################


speak_french = False
knows_python = False

if not speak_french and not knows_python:
    print("To apply, you need to know how to program in Python and speak French")
elif not speak_french:
    print("To apply, you need to speak French")
elif not knows_python:
    print("To apply, you need to know how to program in Python")
else:
    print("You meet the requirements to apply")