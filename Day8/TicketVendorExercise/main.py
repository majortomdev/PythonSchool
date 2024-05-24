
import numbers
def welcome_customer():
    print("*"*50)
    print("*"*10+"    Welcome to the Pharmacy   "+"*"*10)
    print("*" * 50)
    print()
    print("Please take a ticket")
    choice = input("Press P for Perfume, M for Medicine, C for Cosmetics :   ")
    cap = ""

    # if choice == 1:
    #     print(numbers.get_perfume_ticket)
    # elif choice == 2:
    #     print(numbers.get_medicine_ticket)
    # elif choice == 3:
    #     print(numbers.get_cosmetic_ticket)

    numbers.decorate_get_ticket(choice.upper())

def start():

    while True:
        welcome_customer()
        try:
            another_ticket = input('You want another ticket? [Y] [N]').upper()
            ['Y','N'].index(another_ticket)
        except ValueError:
            print("Not valid option")
        else:
            if another_ticket == 'N':
                print("Thanks for your custom")
                break



start()