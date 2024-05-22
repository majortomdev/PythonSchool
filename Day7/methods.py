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
        print(f"The bird is a "+self.species+" and it flies "+str(feet)+" feet high")

tweety = Bird("Green", "Jackdaw")
tweety.chirp()
tweety.chirp_more()
tweety.fly(200)