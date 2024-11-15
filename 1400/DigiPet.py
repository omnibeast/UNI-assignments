# Programer: Saurav Pokharel
# Date: 11/14/2024
# Description:Digipet

print("""
 ____  __  ___  __  ____  ____  ____ 
(    \(  )/ __)(  )(  _ \(  __)(_  _)
 ) D ( )(( (_ \ )(  ) __/ ) _)   )(  
(____/(__)\___/(__)(__)  (____) (__) 
""")

class DigiPet: #defining the Digipet class
    def __init__(self, name):   #setting initial values
        self.name = name
        self.happiness = 100
        self.hunger = 100
        self.health = 100
        self.age = 0

    def play(self): #definig play function
        self.happiness += 5
        self.hunger -= 5
        self.health -= 2
        self.age += 1

    def feed(self):    #defining feed function
        self.hunger += 10
        self.health += 5
        self.age += 1

    def walk(self):     #defining walk function
        self.happiness += 3
        self.hunger -= 5
        self.health += 2
        self.age += 1

    def status(self):   #function to recall the current status of pet
        return f"Happiness: {self.happiness} | Hunger: {self.hunger} | Health: {self.health} | Age: {self.age}" #used some formating learned in CS1030

    def alive(self):    #function to check whether pet is alive or not
        if self.happiness <= 0 or self.hunger <= 0 or self.health <= 0:
            return False
        return True

def main():     #function to run the game
    pet_name = input("What is your DigiPet's name? ")
    pet = DigiPet(pet_name)

    while pet.alive():  #while loop to print options
        print(pet.status())
        print("1. Play")
        print("2. Feed")
        print("3. Walk")
        print("4. Quit")
        choice = input("What would you like to do today? ")

        if choice == "1":
            pet.play()
        elif choice == "2":
            pet.feed()
        elif choice == "3":
            pet.walk()
        elif choice == "4":
            print(f"Goodbye! {pet.name} will miss you.")
            break
        else:
            print("Invalid choice. Please try again.")

    if not pet.alive():
        print(f"Oh no! {pet.name} has passed away.") #printing msg when pet dies


main()      #runing the game
