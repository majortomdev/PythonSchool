from random import choice

# def hangman():
#     gamewords= ['tennis','football','badminton','racketball',
#                 'rallycar','baseball','jiujitsu','billiards']
#
#     word = choice(gamewords)
#     lives = 5
#     hiddenword =[]
#     letters_in_word = []
#
#     for n in word:
#         hiddenword.append('_')
#
#
#     while lives>0:
#         print()
#         print("The word is  :  " + str(hiddenword))
#         print()
#         if '_' not in hiddenword:
#             print()
#             print(f"CONGRATULATIONS you got it, with {lives} lives remaining!" )
#             print("**************************")
#             break
#         print(f"You have {lives} lives left")
#         a_guess = input("Guess a letter in the word:  ")
#         if a_guess in letters_in_word:
#             print("You already guessed that")
#             continue
#         if a_guess in word:
#             letters_in_word.append(a_guess)
#             counter =0
#             print("Correct")
#             for letter in word:
#                 if letter == a_guess:
#                     hiddenword[counter] = letter
#                 counter+=1
#         else:
#             lives-=1
#     if lives<1:
#         print()
#         print("You ran out of lives")
#         print("*****************")
#
# hangman()


def choose_word():
    words = ['donkey', 'albatross', 'daydream','engineer', 'cardigan']

