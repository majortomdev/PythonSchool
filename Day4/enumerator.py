my_list = ['a','b','c']
index=0

for item in my_list:
    print(index, item)
    index+=1


########### OR   OR   OR   OR
print("**************************************************")

for item in enumerate(my_list):
    print(item)



print("**************************************************")

for index, item in enumerate(my_list):
    print(index,item)


print("**************************************************")

####        Or to make a list of TUPLES enumerated from suppliud list::

my_tuples = list(enumerate(my_list))
print(my_tuples)


