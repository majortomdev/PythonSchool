from random import shuffle

#initial list

sticks = ['-','--','---','----']



#mixing sticks
def mix(my_list):
    shuffle(my_list)
    return (my_list)

mix(sticks)
print(sticks)

# choose number
def try_your_luck():
    a_try = ''
    while a_try not in ['1','2','3','4']:
        a_try = input("choose a number: ")

    return int(a_try)

try1 =try_your_luck()
print(try1)


# check players try
def check_try(the_list, the_guess):
    if the_list[the_guess-1] == '-':
        print("You have drawn the short straw. Unlucky")
    else:
        print("You are safe, you didnt draw the short straw")


check_try(mix(sticks),try1)