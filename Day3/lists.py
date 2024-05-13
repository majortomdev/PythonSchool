my_list = [ 'a', 'b', 'c']
print(type(my_list))   ##    prints <class 'list'>
print(len(my_list)) # use len(xxx) to print lenght of xxx

my_list2= ['d', 'e','f']
my_list3= my_list+ my_list2
print(my_list3)
my_list3[0]='alpha'

print(my_list3)
#

fruits = ["apple", "banana", "mango", "cherry", "watermelon"]

deleted_item = fruits.pop(2)
print(deleted_item)
print(fruits)
fruits[2] = deleted_item
print(fruits)




