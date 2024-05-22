class Bird:

    wings = True

    def __init__(self, colour, species):
        self.colour = colour
        self.species = species

    def chirp(self):
        print(f"Tweet Tweet, I am {self.colour}")

    def chirp_more(self):
        print("Tweet Tweet, I am {}".format(self.colour))

    def fly(self, feet):
        print(f"The bird is a " + self.species + " and it flies " + str(feet) + " feet high")

    @classmethod
    def lay_eggs(cls, number):
        print(f'It laid {number} eggs')
        cls.wings = False
        print("iv changed the class attribute wings for all objects of Bird")
        print(Bird.wings)

    @staticmethod
    def look():
        print("The bird looks")

Bird.lay_eggs(12)
Bird.look()
print()

class Character:

    def __init__(self, arrows_amount):
        self.arrows_amount = arrows_amount

    def throw_arrow(self):
        self.arrows_amount = self.arrows_amount - 1


char1 = Character(10)
char1.throw_arrow()
print(f"char1 has {char1.arrows_amount} arrows left")
char1.throw_arrow()
print(f"char1 has {char1.arrows_amount} arrows left")