from random import *

my_random = randint(1,50)
print(my_random)
print("********************************************")
my_random = uniform(5,8)
print(my_random)
print("********************************************")
my_random = round(uniform(1,5),2)
print(my_random)
print("********************************************")
my_random = random()
print(my_random)
print("********************************************")
colours = ['red', 'green','yellow','blue','black']
print(choice(colours))

print("********************************************")

numbers = list(range(5,50,5))
print(numbers)
shuffle(numbers)
print(numbers)



