coffee_prices = [('cappicino', 1.5),
                 ('espresso',3.5),
                 ('mocha',1.9)]

def most_expensive_coffee(list_of_prices):
    highest_price =0
    dearest_brew = ""
    for coffee, price in list_of_prices:
        if price > highest_price:
            highest_price = price
            dearest_brew = coffee
        else:
            pass
    return (f"The dearest coffee is {dearest_brew} at {highest_price}")

print(most_expensive_coffee(coffee_prices))