from random import randint

"The sum of your dice is {suma_dados}. Unfortunate"
"The sum of your dice is {suma_dados}. You have a good chance"
"The sum of your dice is {sum_dice}. It looks like a winning roll"

# def throw_dice():
#     dice1 = randint(1,6)
#     dice2 = randint(1,6)
#     total = dice1+dice2
#     if total<=6:
#         print(f"The sum of your roll is {total}. Unfortunate")
#     elif total<10:
#         print(f"The sum of your roll is {total}. You have a good chance")
#     else:
#         print(f"The sum of your roll is {total}. It looks like a winning roll")
#
#
# throw_dice()


def throw_dice():
    dice1 = randint(1,6)
    dice2 = randint(1,6)
    return(dice1, dice2)

def roll_result(roll1, roll2):
    total = roll1+roll2
    if total<=6:
        return(f"The sum of your dice is {total}. Unfortunate")
    elif total<10:
        return(f"The sum of your dice is {total}. You have a good chance")
    else:
        return(f"The sum of your dice is {total}. It looks like a winning roll")

print("** remove duplicates AND largest number from list **")

list1 = [2 , 6 , 7 , 17, 12 , 12 , 2 , 16, 6, 10]
def reduce_list(numbers):
    updated_nums = []
    highest_val = 0
    for num in numbers:
        if num in updated_nums:
            pass
        else:
            updated_nums.append(num)
            if num > highest_val:
                highest_val = num
    updated_nums.remove(highest_val)
    return updated_nums

print(reduce_list(list1))

print()
print("** HEADS or TAILS toss **")

secret_codes = ['bing',"skub","werk","dawk","hest","murg"]

def toss_coin():
    face = randint(1,2)
    if face == 1:
        return "Heads"
    else:
        return "Tails"

def luck(result, alist):
    if result == 'Tails':
        print("List will self-destruct")
        alist=[]
        return alist
    else:
        print("List was saved")
        return alist

print(luck(toss_coin(), secret_codes))