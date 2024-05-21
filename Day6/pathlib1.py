from pathlib import Path

folder = Path("C:/Users/user/testing/abcde/samp.txt")

if not folder.exists():
    print("This file doesnt exist")
else:
    print("Of course it exists")
    print()
    print(folder.name)
    print(folder.read_text())
    print(folder.suffix)
    print(folder.suffixes)
    print(folder.stem)
    print(folder.anchor + "  is almost the same as  " + folder.drive)
    print(folder.cwd())
    print(folder.drive)
    print()

    print()
    print("*************************************")
    print()


