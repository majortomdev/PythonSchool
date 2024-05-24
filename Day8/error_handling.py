def addition():
    n1 = int(input("The first number:   "))
    n2 = int(input("The second number:   "))
    print(n1 +n2)
    print("Thanks for adding " +n1)



try:
    addition()

except TypeError:
    print("ERROR: You are trying to concatenate different types")

except ValueError:
    print("ERROR: This is not a proper number")

else:
    print("You did well my son")

finally:
    print("Thats all for now folks")


def ask_number():
    while True:

        try:
            number = int(input("Enter a number:  "))

        except:

            print("That is not a number")

        else:
            print(f"You have entered number {number}")
            break

    print("Thank you")

ask_number()