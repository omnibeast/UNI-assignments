# Programmer Kim Murphy
# Shopping list.  Allow user to enter their items.
# View items


list = [] #emptylist creation


def LoadList(): #function to load file
    print("Loading Groceries.txt")
    try:
        f = open("Groceries.txt", 'r')  #opening the file
        for line in f:                  #going through each line in the file
            line = line.strip()
            list.append(line)
        f.close()                       #closes the file
    except FileNotFoundError as err:    #exception if file is not found
        print(err)
        print("Creating Groceries.txt")
        f = open("Groceries.txt", "w")  #Create the file
        f.close()


def ViewList():                         #function to show item in the list
    print("List Items")
    for i in list:
        print(i)


def RemoveItem():                       #function to remove item from the list and update the text file
    try:
        item = input("What item do you want to remove? ")
        list.remove(item)               #remove item from the list
        SaveList()                      #rewrite the list to the file
    except ValueError as err:
        print("Item not in list")


def AddItem():                          #function to add item to list
    item = input("What item do you want to add: ")
    list.append(item)                   #adding item to the list
    try:
        f = open("Groceries.txt", 'a')  #opening the file to append
        f.write(item + "\n")            #writing to the file   
        f.close()                       #closes the file
    except FileNotFoundError as err:
        print(err)

def SaveList():                         #write the list to the file
    try:
        f = open("Groceries.txt", "w")  #opening file to write
        for i in list:                  #iterate the list
            f.write(i + "\n")           #write each item, adding an endline
        f.close()                       #closing file
    except FileNotFoundError as err:
        print(err)


def Menu():                             #prints the menu
    print("1. Add Item")
    print("2. Remove Item")
    print("3. Quit")


LoadList()                              #calling the load list function to load list from the list


choice = 0
while choice != 3:
    ViewList()                          #calling the view list function
    Menu()
    try:
        choice = int(input("Choose one:"))
        if choice == 1:
            AddItem()
        elif choice == 2:
            RemoveItem()
        elif choice == 3:
            print("thanks for using ListGen")
        else:
            raise Exception("Not a valid number")
    except ValueError as err:
        print("Enter a number between 1 and 3")
    except:
        print("Enter a number between 1 and 3")
