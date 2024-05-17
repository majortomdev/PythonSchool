def return_distincts(num1,num2,num3):

    a_sum = num1+num2+num3
    a_list = [num1, num2, num3]

    if a_sum > 15:
        return max(a_list)
    elif a_sum <10:
        return min(a_list)
    else:
        a_list.sort()
        return a_list[1]



print(return_distincts(1,5,6))
