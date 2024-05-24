# def uppercase(text):
#     print(text.upper())
#
#
# def lowercase(text):
#     print(text.lower())
#
#
# print("Hello")
# uppercase("Today is Thursday")
# print("Goodbye")

#####********************************************

# def change_letters(type):
#     def lowercase(text):
#         print(text.lower())
#
#     def uppercase(text):
#         print(text.upper())
#
#     if type == 'upp':
#         return uppercase
#     elif type == 'low':
#         return lowercase
#
# operation = change_letters('lo')
#
# operation('word')


#####********************************************


def decorate_greeting(funnction):

    def another_function(word):

        print('Hello')
        funnction(word)
        print("Goodbye")

    return another_function

@decorate_greeting
def uppercase(text):
    print(text.upper())

@decorate_greeting
def lowercase(text):
    print(text.lower())

uppercase('Python')
lowercase('Python')
