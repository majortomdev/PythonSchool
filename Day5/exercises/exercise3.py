# def close_up_zeros(*args):
#     count_zeroes = 0;
#     indx=0
#     args_list=[]
#     # for num in args:
#     #
#     #     args_list.append(num)
#     #print(args[1])  just testing
#
#     count = 0
#     for count, item in enumerate(args, start=1):
#         print(count, item)
#
#
#
#
# close_up_zeros(2,11,23,66,5,76)



#           ABOVE is my early tries

def close_up_zeroes(*args):
    counter = 0

    for n in args:

        if counter+1 == len(args):# this is the silver bullet
            return False#  here

        elif args[counter] == 0 and args[counter+1] == 0:
            return True
        else:
            counter+=1
    return False

print(close_up_zeroes(1,0,4,0,7,0,7,0))