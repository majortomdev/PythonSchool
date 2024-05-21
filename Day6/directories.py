import os
from pathlib import Path

path = os.getcwd()
print(path)
path = os.chdir("C:\\simpleStuff")
print(path)
file = open("sample_py_file.txt")
print(file.read())

#.....to make a directory
# path = os.makedirs("C:\\simpleStuff\\new_py_folder")


path = "C:\\Users\\user\\testing\\testit.txt"

element = os.path.basename(path)
print(element)
print()
print("vvv--  ** or create a tuple with path.split  **  --vvvv")
element = os.path.split(path)
print(element)


print("***  to DELETE a directory   ****")
#os.rmdir("C:\\Users\\user\\testing\\sample")

print()
print("****************************************")
print()
print("## a way to use forward slashes to do same ##")

folder = Path("C:/Users/user/testing/abcde") / "samp.txt"

my_file = open(folder)
print(my_file.read())