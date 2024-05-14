def check_3_digits(number):
    return number in range(100,1000)

result = check_3_digits(555)
print(result)

print("*****************************************")
print("***  to run same method but on list, true if even 1 hit ***")
num_list = [12, 3643, 256, 6597, 654, 7654, 324]

def check_3_digits_list(list1):
    for n in list1:
        if n in range(100,1000):
            return True
        else:
            pass
    return False

print(check_3_digits_list(num_list))

print("*****************************************")
print("***  this time, return a list of all that are 3 digit ***")

def check_3_return_in_list(list1):
    list_of_3s = []

    for n in list1:
        if n in range(100,1000):
            list_of_3s.append(n)
        else:
            pass

    return list_of_3s

print(check_3_return_in_list(num_list))

print("*****************************************")
print("***  this time, total all items in list in range 1 - 999 ***")
def sum_less(list1):
    total = 0
    for n in list1:
        if n in range(1, 1000):
            total += n
        else:
            pass
    return total
numbers = [23, 2342, 57, 57, 29, 125, 658, 4349, 3402, 3402]
print(sum_less(numbers))
print("*****************************************")
print("***  this time, count no of EVEN numbers ***")
numbers_oe = [ 34, 37, 12, 15, 19, 23, 24]
def count_even (list1):
    count = 0;
    for n in list1:
        if n%2 ==0:
            count+=1
        else:
            pass
    return count
print(count_even(numbers_oe))
print("*****************************************")
print("***  make EVENS into a dict of list index: value ***")

def dict_of_evens(list1):
    dict = {}
    count = -1
    for n in list1:
        count+=1
        if n%2==0:
            dict[count] = n
        else:
            pass
    return dict
print(dict_of_evens(numbers_oe))