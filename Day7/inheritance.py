class Animal:

    def __init__(self, age, colour):
        self.age = age
        self.colour = colour
    def born(self):
        print("This animal has been born")

    def talk(self):
        print("This animal makes a sound")


class Bird(Animal):
    def talk(self):
        print("This bird says cheepcheep")
    pass

tweety = Bird(7,"Grey")

tweety.born()
tweety.talk()
print(tweety.colour)

########################################################
#exercise 1:
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


class Student(Person):
    pass