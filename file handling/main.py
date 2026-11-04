from pathlib import Path
import os


def readfileandfolder():
    path = Path('')
    items = list(path.rglob('*'))
    for i,items in enumerate(items):
        print(f"{i+1} : {items}")

def createfile():
    try:
        readfileandfolder()
        name = input("Please tell your file name: ")
        p=Path(name)
        if not p.exists():
            with open(p,"w") as fs:
                data = input("What do you want to write: ")
                fs.write(data)
            print("FILE CREATED SUCCESSFULLY")
        else:
            print("This file already exists")

    except Exception as err:
        print(f"An exception occured as {err}")

def readfile():
    try:
        readfileandfolder()
        name = input("Which file you want to read? ")
        p = Path(name)
        if p.exists and p.is_file():
            with open(p,'r') as fs:
                data = fs.read()
                print(data)

            print("READED SUCCESSFULLY")
        else:
            print("The file doesn't exists")
    except Exception as err:
        print(f"An error occured as {err}")

def updatefile():
    try:
        readfileandfolder()
        name = input("Tell which file you want to update: ")
        p=Path(name)
        if p.exists() and p.is_file():
            print("Press 1 for changing the name of your file")
            print("Press 2 for overwriting the data of your file")
            print("Press 3 for appending some content in your file")

            res = int(input("Tell your choice: "))
            if res == 1:
                name2 = input("Tell your new name of the file: ")
                p2 = Path(name2)
                p.rename(p2)

            if res == 2:
                with open(p,'w') as fs:
                    data = input("What you want to write?(this will overwrite the data): ")
                    fs.write(data)
            
            if res == 3:
                with open(p,'a') as fs:
                    data = input("What you want to append: ")
                    fs.write(" " + data)
    except Exception as err:
        print(f"An exception occured as {err}")

def deletefile():
    try:
        readfileandfolder()
        name = input("Which file you want to delete? ")
        p=Path(name)
        if p.exists() and p.is_file():
            os.remove(name)
            print("FILE REMOVED SUCCESSFULLY")
        else:
            print("No such file exists")
    except Exception as err:
        print(f"An exception occured as {err}")


print("Press 1 for creating a file")
print("Press 2 for reading a file")
print("Press 3 for updating a file")
print("Press 4 for deleting a file")

check = int(input("Enter your choice: "))

if check == 1:
    createfile()

if check == 2:
    readfile()

if check == 3:
    updatefile()

if check == 4:
    deletefile()