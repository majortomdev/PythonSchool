name = input("What is your employee name: ")

sales = int(input("What sales have you made this week? "))

commission = round(sales*13/100, 2);
#commissionb = (commission*13)/100;
print(type(commission))
print(f"Congratulations {name}, this week you have earned commission of ${commission}")