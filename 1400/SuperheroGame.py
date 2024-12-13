"""
Programer: Saurav Pokharel
Date: 11/27/2024
Description: game 
"""
print("""
 _____                       _                      _   _        _   _ _ _ _             
/  ___|                     | |                    | | | |      | | | (_) | |            
\ `--. _   _ _ __   ___ _ __| |__   ___ _ __ ___   | | | | ___  | | | |_| | | __ _ _ __  
 `--. \ | | | '_ \ / _ \ '__| '_ \ / _ \ '__/ _ \  | | | |/ __| | | | | | | |/ _` | '_ \ 
/\__/ / |_| | |_) |  __/ |  | | | |  __/ | | (_) | \ \_/ /\__ \ \ \_/ / | | | (_| | | | |
\____/ \__,_| .__/ \___|_|  |_| |_|\___|_|  \___/   \___/ |___/  \___/|_|_|_|\__,_|_| |_|
            | |                                                                          
            |_|                                                                          
""")

import random

class Player:
    def __init__(self, name): #initializating initial values
        self.name = name
        self.life_points = 100
        self.strength = 0

    def set_strength(self): #defining random strength
        self.strength = random.randint(1, 20)

    def receive_damage(self, damage):   #function to damage life
        self.life_points -= damage

    def is_alive(self):     #function to check if player is alive
        return self.life_points > 0

def battle(player1, player2):   #battle function
    player1.set_strength()  #setting player strength
    player2.set_strength()
    print(f"{player1.name} strength: {player1.strength}, {player2.name} strength: {player2.strength}")

    #determining the winner and appying damage to the loser.
    if player1.strength > player2.strength:     
        damage = player1.strength - player2.strength
        player2.receive_damage(damage)
        print(f"{player2.name} has {damage} points of damage.")
    elif player2.strength > player1.strength:
        damage = player2.strength - player1.strength
        player1.receive_damage(damage)
        print(f"{player1.name} has {damage} points of damage.")
    else:
        print("It's a tie! No damage this round.")

def main(): #main function to run the game
    superhero_name = input("Enter SuperHero Name: ")
    villain_name = input("Enter Villan Name: ")

    superhero = Player(superhero_name) #create a superhero player 
    villain = Player(villain_name)

    while superhero.is_alive() and villain.is_alive():  #main loop game continus as long as both player alive
        print(f"\n{superhero.name} Life Points: {superhero.life_points}")
        print(f"{villain.name} Life Points: {villain.life_points}")
        print(f"{superhero.name} Your Turn!")
        choice = input("Press h to hit, q to quit: ").lower()

        if choice == 'h':
            battle(superhero, villain)
        elif choice == 'q':
            print("Nice battle! Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

        if not villain.is_alive():
            print(f"{villain.name} has been defeated! {superhero.name} wins!")
            break

        print(f"\n{villain.name} Your Turn!")
        choice = input("Press h to hit, q to quit: ").lower()

        if choice == 'h':
            battle(villain, superhero)
        elif choice == 'q':
            print("Nice battle! Thanks for playing!")
            break
        else:
            print("Invalid choice. Please try again.")

        if not superhero.is_alive():
            print(f"{superhero.name} has been defeated! {villain.name} wins!")
            break

main()