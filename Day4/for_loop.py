my_list = ['a', 'b', 'c']

for letter in my_list:
    letterIndex = my_list.index(letter)+1
    print(letter+". Project:  "+str(letterIndex))


my_list2 = ['Paul','Martin','Brian','Katherine','Patricia','Francis','Gerard']

print("############################################################")
for name in my_list2:
    if name.startswith('M') or name.startswith('B'):
        print(name)
    else:
        print("The others")

print("############################################################")

numbers = [1,2,3,4,5]
my_value = 0

for number in numbers:
    #my_value = my_value+number
    my_value+=number

print(my_value)

print("############################################################")

word = 'python'

for letter in word:
#for letter in 'word':
    print(letter)

print("############################################################")

for a,b in [[1,2], [3,7],[5,6]]:
    print(a)
    print(b)