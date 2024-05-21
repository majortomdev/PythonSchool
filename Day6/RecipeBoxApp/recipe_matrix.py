import os
from pathlib import Path
from os import system

user_selection=0
finish_program = False
my_path = Path(Path.home(), 'Recipes')
recipes = Path(my_path).glob('*.txt')
def count_recipes(path):
    counter = 0

    for txt in Path(path).glob('**/*.txt'):
        counter += 1

    return counter

def start():
    system('cls')
    print('*' *50)
    print('*' *5 +"   Welcome to the recipe administrator  "+'*'*5)
    print('*' *50)
    print('\n')
    print(f'The recipes are in {my_path}')
    print()
    print(f'There are {count_recipes(my_path)} recipes in total')

    user_selection = 'x'
    while not user_selection.isnumeric() or int(user_selection) not in range(1,7):
        print("Choose from the following: ")
        print('''
        [1] Read Recipe
        [2] Create Recipe
        [3] Create Category
        [4] Delete Recipe
        [5] Delete Category
        [6] End Program
        ''')
        user_selection = input()

    return int(user_selection)
def show_categories(path):
    print("Categories: ")
    categories_path = Path(path)
    categories_list = []
    counter = 1

    for folder in categories_path.iterdir():
        folder_str = str(folder.name)
        print(f'[{counter}] - {folder_str}')
        categories_list.append(folder)
        counter += 1

    return categories_list

def choose_category(categories):
    correct_choice = 'x'
    while not correct_choice.isnumeric() or int(correct_choice) not in range(1, len(categories)+1):
        correct_choice = input('\nChoose a category: ')

    return categories[int(correct_choice)-1]

def show_recipes(path):
    print("These are the recipes: ")
    recipes_path = Path(path)
    recipes_list = []
    counter = 1

    for recipe in recipes_path.glob('*.txt'):
        recipe_str = str(recipe.name)
        print(f'[{counter}] - {recipe_str}')
        recipes_list.append(recipe)
        counter += 1

    return recipes_list

def choose_recipe(a_list):
    recipe_choice = 'x'

    while not recipe_choice.isnumeric() or int(recipe_choice) not in range(1, len(a_list)+1):

        recipe_choice = input('\nChoose a recipe: ')
    #print("*********  "+list[input(recipe_choice)-1].name )
    return a_list[int(recipe_choice)-1]

def read_recipe(recipe):
    print(Path.read_text(recipe))

def create_recipe(path):
    exists = False

    while not exists:
        print("Write the name of your recipe: ")
        recipe_name = input() + '.txt'
        print("Write your new recipe: ")
        recipe_content = input()
        new_path = Path(path, recipe_name)

        if not os.path.exists(new_path):
            Path.write_text(new_path, recipe_content)
            print(f"Your recipe {recipe_name} has been created")
            exists = True
        else:
            print("Sorry, that recipe already exists!")

def create_category(path):
    exists = False

    while not exists:
        print("Write the name of your new category: ")
        category_name = input()
        new_path = Path(path, category_name)

        if not os.path.exists(new_path):
            Path.mkdir(new_path)
            print(f"Your new category {category_name} has been created")
            exists = True
        else:
            print("Sorry, that category already exists!")

def delete_recipe(recipe):
    Path(recipe).unlink()
    print(f"The recipe {recipe.name} has been deleted")

def delete_category(category):
    Path(category).rmdir()
    print(f"The category {category.name} has been removed")

def return_to_beginning():
    return_choice = 'x'

    while return_choice.lower() != 'b':
        return_choice = input("\nPress 'b' to return to the menu: ")

while not finish_program:
    user_selection = start()

    if user_selection ==1:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        my_recipes = show_recipes(my_category)
        if len(my_recipes)<1:
            print("This categorys got zero recipes in it")
        else:
            my_recipe = choose_recipe(my_recipes)
            read_recipe(my_recipe)
        return_to_beginning()
        pass

    elif user_selection == 2:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        create_recipe(my_category)
        return_to_beginning()
        pass

    elif user_selection == 3:
        create_category(my_path)
        return_to_beginning()
        pass

    elif user_selection == 4:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        my_recipes = show_recipes(my_category)
        if len(my_recipes)<1:
            print("This categorys got zero recipes in it")
        else:
            my_recipe = choose_recipe(my_recipes)
            delete_recipe(my_recipe)
        return_to_beginning()
        pass

    elif user_selection == 5:
        my_categories = show_categories(my_path)
        my_category = choose_category(my_categories)
        delete_category(my_category)
        return_to_beginning()
        pass

    elif user_selection == 6:
        finish_program = True
        pass