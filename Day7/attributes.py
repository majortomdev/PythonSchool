class Bird:

    flyable = True      #CLASS Variable

    def __init__(self, colour):
        self.colour = colour        #INSTANCE Variable


my_bird = Bird('black')

print("Its "+my_bird.colour+", its  "+str(my_bird.flyable)+" that it can fly")