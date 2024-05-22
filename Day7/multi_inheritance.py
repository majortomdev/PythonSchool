class Father:
    def talk(self):
        print("Hello")

class Mother:
    def laugh(self):
        print("Haha piece of cake")

    def talk(self):
        print("How are you")

class Child(Mother, Father):
    pass

class Grandchild(Child):
    pass


my_grandchild = Grandchild()

my_grandchild.talk()
my_grandchild.laugh()

print(Grandchild.__mro__)



################################
ex1


class Father():
    def work(self):
        print("Working in the Public Hospital")

    def laugh(self):
        print("Ha Ha Ha!")


class Mother():
    def work(self):
        print("Working in the Public Prosecutor's Office")


class Daughter(Mother, Father):
    pass