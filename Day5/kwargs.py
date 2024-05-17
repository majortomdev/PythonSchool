def a_sum(**kwargs):

    for key, value in kwargs.items():
        print(f"{key} = {value}")

a_sum(x=3,y=5,z=2)
print()
print("*************************************")
print()

def b_sum(number1, number2, *args, **kwargs):

    print(f"The first number is {number1}")
    print(f"The second number is {number2}")
    tick=1
    for arg in args:
        print(f"arg{tick} = {arg}")
        tick+=1

    for key, value in kwargs.items():
        print(f"{key} = {value}")

b_sum(25,50,100,200,300,400,500,x='one',y='two',z='three')

print()
print("*********  Count # of args passed  ********")
print()


def number_attributes(**kwargs):
    qty = 0
    for key in kwargs:
        qty += 1
    return qty

res = number_attributes(x='one',y='two',z='three')
print(res)
print()
print("*********  return list of values given in 'keywords'  ********")
print()
def list_attributes(**kwargs):
    arg_values = []
    for key, value in kwargs.items():
        arg_values.append(value)
    return arg_values

print(list_attributes(x='one',y='two',z='three'))
print()
print("*********  function to print out characteristics as passed  ********")
print()

def describe_person(name, **kwargs):
    print(f"Characteristics of {name}:")
    for key, value in kwargs.items():
        print(f"{key}: {value}")

describe_person("Gerard", hair_colour="black", eye_colour="blue",
                height="5 9", profession = "developer")