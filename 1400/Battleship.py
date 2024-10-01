"""
Programer: Saurav Pokharel
Date: 09/27/2024
Description: Battleship Game. 
"""


import math
import random

print("""
██████╗  █████╗ ████████╗████████╗██╗     ███████╗███████╗██╗  ██╗██╗██████╗ 
██╔══██╗██╔══██╗╚══██╔══╝╚══██╔══╝██║     ██╔════╝██╔════╝██║  ██║██║██╔══██╗
██████╔╝███████║   ██║      ██║   ██║     █████╗  ███████╗███████║██║██████╔╝
██╔══██╗██╔══██║   ██║      ██║   ██║     ██╔══╝  ╚════██║██╔══██║██║██╔═══╝ 
██████╔╝██║  ██║   ██║      ██║   ███████╗███████╗███████║██║  ██║██║██║     
╚═════╝ ╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚══════╝╚══════╝╚═╝  ╚═╝╚═╝╚═╝     
                                                                             
""")

def submarine_hunt():

    random_x = random.randint(1, 10) #generate random coordinates for the submarine
    random_y = random.randint(1, 10)

    missiles_remaining = 10

    while missiles_remaining > 0:
        #getting X and Y coordinate from player
        x = int(input("Enter X coordinate:"))
        y = int(input("Enter Y coordinate:"))

        distance = math.sqrt((x - random_x) ** 2 + (y - random_y) ** 2) #calculating the Euclidean distance
        distance = round(distance, 2)

        if distance == 0:
            print("Successful Hit!")
            break
        else:
            print("Miss:",distance,"meters away.",missiles_remaining, "missiles remaining.")
            missiles_remaining -= 1

        # Check if the submarine was hit or escaped
        if missiles_remaining == 0:
            print("The submarine got away!")

submarine_hunt()