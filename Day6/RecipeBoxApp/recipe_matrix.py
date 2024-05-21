import os
from pathlib import Path
from os import system

user_selection=0
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
    while not correct_choice.isnumeric() or correct_choice not in range(1, len(categories)+1):
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


def choose_recipes(list):
    recipe_choice = 'x'

    while not recipe_choice.isnumeric() or recipe_choice not in range(1, len(list)+1):
        recipe_choice = input('\nChoose a recipe: ')

    return list[input(recipe_choice)-1]


start()

if user_selection ==1:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)
    my_recipes = show_recipes(my_category)
    my_recipe = choose_recipes(my_recipes)
    pass

elif user_selection == 2:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)

    pass

elif user_selection == 3:


    pass

elif user_selection == 4:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)
    my_recipes = show_recipes(my_category)
    my_recipe = choose_recipes(my_recipes)

    pass

elif user_selection == 5:
    my_categories = show_categories(my_path)
    my_category = choose_category(my_categories)

    pass