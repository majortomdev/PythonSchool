import  re


# text = 'If you need help call (658)-598-9977 any time for online help'
#
# pattern = 'help'
#
# #search = re.findall(pattern,text)# returns list
#
# for finding in re.finditer(pattern, text):
#     print(finding.span())


###*******************   PHONE NUMBER     *************


# text = 'call to 564-885-6588 right now'
#
# pattern1 = r'\d\d\d-\d\d\d-\d\d\d\d'
# pattern2 = r'\d{3}-\d{3}-\d{4}'         #exact same as patten1
# pattern3 = re.compile(r'\d{3}-\d{3}-\d{4}')     #same again
#
# result = re.search(pattern1, text)
#
# print(result.span())
# #print(text[result.span().index(0),result.span().index(1)])



###*******************   PASSWORD     *************

# secure = False
# password = ""
# while not secure:
#     password = input("Password:  ")
#
#
#     pattern = r'\D{1}\w{7}'     #must start with a number and be 8 characters long
#
#     check = re.search(pattern, password)
#     if not check:
#         print("Invalid, password must not start with a number and be at least 8 characters long")
#         pass
#     else:
#         print("Thank you, ******** is saved as your new password")
#         secure = True





###*******************   PASSWORD     *************


text = 'Saturday and sunday this store is closed'

search = re.search(r'sunday|monday', text)
search2 = re.search(r'....lose.', text)
search3 = re.search(r'^\D', text)   #  ^ first character not a digit?
search4 = re.search(r'\D$', text)   #  $ last character not a digit?
search5 = re.findall(r'[^\s]',text)

print(search)
print(search2)
print(search3)
print(search4)

print('.'.join(search5))
print(''.join(search5))



def check_email(email):
# "Ok"
# "The email address is incorrect"

    pattern = r'\w+@\w+\.com$' # as in -> 1 or more chars b4 @, @itself, 1 or more chars after @, ending in .com
    valid = re.search(pattern, email)
    if valid:
        print("Ok")
    else:
        print("The email address is incorrect")


check_email("j@6.com")


def check_pc(pc):
    pattern = r'\w{2}\d{4}'

    valid = re.search(pattern, pc)
    if valid:
        print("Ok")
    else:
        print("The zip code entered is not correct")

check_pc("sa6237")






