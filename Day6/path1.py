from pathlib import Path

base = Path.home()
guide = Path(base, 'Europe', 'France', Path('Paris', 'Eiffel_Tower.txt'))
#guide2 = guide.with_name('Notre_Dame.txt')

print(guide.parent.parent)
#print(guide2)

print()
print("********************************")
print()


guide3 = Path(Path.home(), 'Europe')

for txt in Path(guide).glob('*.txt'):
    print(txt)


print()
print("****************************")
print()
my_path = Path('C:/Users/User/Desktop/Python Course') / 'Quiz Day 6' / 'Question 1'
folder = my_path.parents[3]
print(folder)