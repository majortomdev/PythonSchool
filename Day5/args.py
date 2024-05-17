def a_sum(*bits):
    total = 0;
    for arg in bits:
        total+=arg
    return total

print(a_sum(55,7, 5, 11, 77))

print()
print("***************  sum of each item squared  **********")
numbers = [2, 6 , 8 , 9]
def sum_squares(*args):
    total =0
    for arg in args:
        total+= arg*arg
    return total

result = sum_squares(*numbers)
print(result)

print()
print("***************  sum of absolutes  **********")

def absolute_sum(*args):
    total=0
    for arg in args:
        total+=abs(arg)
    return total


result = absolute_sum(-4,1,8,-8,-5)
print(result)

print()
print("************************************")

def personal_numbers(*args):
    name = ""
    total = 0
    for arg in args:
        if len(name) == 0:
            name=arg
        else:
            total+= arg
    print(f"{name}, the sum of your numbers is {total}")
personal_numbers("Desmond",15,25,5,20,35)