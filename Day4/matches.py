series = "N-03"

'''if series == "N-01":
    print("Samsung")
elif series == "N-02":
    print("Nokia")
elif series == "N-03":
    print("Motorola")
else:
    print("This product does not exist")'''

match series:

    case "N-01":
        print("Samsung")
    case "N-02":
        print("Nokia")
    case "N-03":
        print("Motorola")
    case _:
        print("This product does not exist")

print()
print("******************************************")
print()

client = {'name': 'Joseph',
          'age':46,'occupation':'developer'}
movie = {'title':'Matrix',
         'credits':{'main_star':'Keanu Reeves',
                    'director':'Lana & Lilly Wachowski'
         }}
items = [client, movie, 'book']

for i in items:
    match i:
        case{'name':name,
             'age':age,
             'occupation':occupation}:
            print("It is a client")
            print(name, age, occupation)
        case{'title':title,
             'credits':{'main_star':main_star,
                        'director':director}}:
            print("This is a movie")
            print(title,main_star, director)
        case _:
            print("I dont know what this is")