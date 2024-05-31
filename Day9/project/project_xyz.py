from datetime import datetime
import re
import os
import time
from pathlib import Path
import math

today = datetime.now()

nos_found = 0
my_pattern = r'N\D{3}-\d{5}'
path = 'C:\\Users\\user\\Desktop\\Python\\pythonProject\\Day9\\project\\My_Big_Directory'
serialDict = {}
numbers_found = []
files_found = []


def find_number(file, pattern):
    this_file = open(file, 'r')
    text = this_file.read()
    if re.search(pattern, text):
        return re.search(pattern, text)
    else:
        return ''


def create_lists():
    for folder, subfolder, file in os.walk(path):
        for a in file:
            result = find_number(Path(folder, a), my_pattern)
            if result != '':
                numbers_found.append(result.group())
                files_found.append(a.title())


# for folder, subfolder, files in os.walk(path):
#     for f in files:
#         fx = open(f, 'r')
#         while(fx.readline()):
#             found = re.search(pattern, fx.readline())
#             if(found):
#                 serialDict[f]=fx.readline(found.start(),found.end())
#                 nos_found+=1
#             break


def show_all():
    index = 0
    print("-" * 50)
    print(f'Search date: {today.month}/{today.day}/{today.year}')
    print()
    print("FILE" + "\t\t\t" + "SERIAL NO.")
    print("-" * 4 + "\t\t\t" + "-" * 10)
    for a in files_found:
        print(f'{a}\t\t{numbers_found[index]}')
        index += 1

    print()
    print(f"Numbers found: {len(numbers_found)}")


create_lists()
show_all()
