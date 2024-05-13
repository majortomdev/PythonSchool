names = ['Hannah',"Bruce","Tony"]

ages = [65, 29, 42]

my_list_zipped = list(zip(names,ages))

print(my_list_zipped)

print("******************************************************")
capitals = ["Berlin", "Tokyo", "Paris", "Helsinki", "Ottawa", "Canberra"]
countries = ["Germany", "Japan", "France", "Finland", "Canada", "Australia"]

my_list = list(zip(capitals, countries))


for city, country in my_list:
    print(f"The capital of {country} is {city}")

print("******************************************************")
brands = [ "Sony", "Yamaha", "Toyota", "Ford", "Logik"]
products = [ "Walkman", "Bass Guitar", "Celica", "Destroyer", "Mouse" ]

my_zip = zip(brands, products)  ## makes object of class 'zip'
my_zipped_list = list(zip(brands, products)) ## makes obj of class 'list'

for make, model in my_zip:
    print(f"{make} is the company behind the {make} {model}")

print("******************************************************")


spanish = ["uno", "dos", "tres", "cuatro", "cinco"]
portuguese = ["um", "dois", "três", "quatro", "cinco"]
english = ["one", "two", "three", "four", "five"]

numbers = list(zip(spanish,portuguese,english))
print(numbers)