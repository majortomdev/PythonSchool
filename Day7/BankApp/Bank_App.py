from os import system

accounts = []
#action_choice=0

class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname

class Customer(Person):
    def __init__(self, firstname, lastname, account_number, balance):
        super().__init__(firstname, lastname)
        self.account_number = account_number
        self.balance = balance

    def __str__(self):
        return f'{self.firstname} {self.lastname} has a balance of {self.balance}'

    def deposit(self, amount):
        self.balance += amount
        print(f'Your mew balance is {self.balance}')

    def withdraw(self, amount):
        if amount > self.balance:
            print("Sorry, you dont have enough left in your account for this transaction")
            print(f'Your balance is {self.balance}')
        else:
            self.balance -= amount
            print(f'Your new balance is {self.balance}')

def bank_action(cust):
    stay_connected = True
    print(cust)
    while stay_connected:
        action_choice = int(input('''Would you like to: 
        Deposit[1]
        Withdraw[2] or
        Exit[3]
        Please Enter 1, 2 or 3:   '''))
        if action_choice == 1:
             amount = int(input("How much would you like to deposit?"))
             cust.deposit(amount)
        elif action_choice == 2:
             amount = int(input("How much would you like to withdraw?"))
             cust.withdraw(amount)
        elif action_choice ==3:
            print("Thanks and good day")
            stay_connected=False
        else:
            pass


def start():
    system('cls')
    print('*' *50)
    print('*' *5 +"   Welcome to the JK Bank  "+'*'*5)
    print('*' *50)

    f_name = input("What is your first mame: ")
    l_name = input("What is your last mame: ")
    a_number = input("What is your account number: ")
    bal = int(input("What is your current balance"))


    customer_a = Customer(f_name,l_name,a_number,bal)
    accounts.append(customer_a)
    #print(customer_a)
    bank_action(customer_a)


start()


