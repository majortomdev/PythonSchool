word = 'python'
my_list = []

for letter in word:
    my_list.append(letter)

print(my_list)
print()
print("**********  same result easier   *************")

word = "java"
my_list = [ff for ff in word]
print(my_list)

print()
print("*******************************************")
print()

my_list = [n for n in range(0,21,2)]
print(my_list)

print()
print("*******************************************")
print()
my_list = [n for n in range(0,21,2) if n*2>14]
print(my_list)

print()
print("*******************************************")
print()
my_list = [n if n*2>14 else 'N' for n in range(0,21,2) ]
print(my_list)

print()
print("***************  MEASUREMENTS transformed    ****************")
print()

feet = [10 ,25 ,17, 38, 12]
meters = [round(0.3048*dist,3) for dist in feet]
print(meters)


