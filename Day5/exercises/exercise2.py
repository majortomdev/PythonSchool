def unique_letters(wordley):
    alphabet_list=[]
    for letter in wordley:
        if letter in alphabet_list:
            pass
        else:
            alphabet_list.append(letter)
#set would have been bit shorter but then wed have to cast it as
#a list in order to sort it !!!
    alphabet_list.sort()
    return alphabet_list

print(unique_letters("pineapple"))