"""
Programer: Saurav Pokharel
Date: 12/01/2024
Description: A program that allows customers to view the menu, place an order, and display the order summary. 
"""

# MenuItem class to represent individual menu items
class MenuItem:
    def __init__(self, name, price): #initialize menu item attributes.
        self.name = name
        self.price = price

# Order class to handle customer orders
class Order:
    def __init__(self): #creating an empty order list.
        self.items = []

    def add_item(self, menu_item):  #method to add item to list.
        self.items.append(menu_item)

    def calculate_total(self):      #calculating the total cost of order.
        total = 0  
        for item in self.items:
                total += item.price
        return total

    def display_order(self):    #function to print order summary
        print("Your Order:")
        for item in self.items:
            print(f"- {item.name}: ${item.price:.2f}")
        print(f"Total: ${self.calculate_total():.2f}")

#Restaurant class to manage the menu and orders
class Restaurant:
    def __init__(self):
        self.menu = []  #list to store menu item

    def add_menu_item(self, name, price):   #method to add items to menu
        self.menu.append(MenuItem(name, price))

    def display_menu(self): #function to display menu
        print("Menu:")
        for index, item in enumerate(self.menu, start=1):
            print(f"{index}. {item.name} - ${item.price:.2f}")

# Main program
def main():
    restaurant = Restaurant()   #creating instance of the resturant class

    restaurant.add_menu_item("Burger", 8.99) #adding items to menu
    restaurant.add_menu_item("Pizza", 12.50)
    restaurant.add_menu_item("Salad", 6.75)
    restaurant.add_menu_item("Soda", 2.50)

    print("""
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ 
 |R|e|s|t|a|u|r|a|n|t| |O|r|d|e|r|i|n|g| |S|y|s|t|e|m| 
 +-+-+-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+-+-+ +-+-+-+-+-+-+ 
""")

    while True: #main loop to keep program running
        print("\nMain Menu")
        print("1. View Menu")
        print("2. Place an Order")
        print("3. Exit")

        choice = int(input("Choose an option: "))

        if choice == 1: #displaying menu if user choose option 1
            restaurant.display_menu()
        elif choice == 2:   #creating an order if user choose option 2
            order = Order()
            while True: #loop inorder to allow customer to add multiple item to order.
                restaurant.display_menu()
                item_choice = int(input("Enter the number of the item to add to your order (0 to finish): "))
                if item_choice == 0:
                    break
                elif 1 <= item_choice <= len(restaurant.menu): #if the user inpuit is in valid range it will add item to list.
                    selected_item = restaurant.menu[item_choice - 1]
                    order.add_item(selected_item)
                    print(f"{selected_item.name} added to your order.")
                else:
                    print("Invalid choice. Please try again.")

            order.display_order()

        elif choice == 3:
            print("Thank you for visiting! Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__": 
    main()

