"""
Programer: Saurav Pokharel
Date: 10/01/2024
Description: Candy Guessing Game with Random Generation. 
"""
import random

print("""
   ______                __         _          __  __                __              
  / ____/___ _____  ____/ /_  __   (_)___     / /_/ /_  ___         / /___ ______    
 / /   / __ `/ __ \/ __  / / / /  / / __ \   / __/ __ \/ _ \   __  / / __ `/ ___/    
/ /___/ /_/ / / / / /_/ / /_/ /  / / / / /  / /_/ / / /  __/  / /_/ / /_/ / /        
\____/\__,_/_/ /_/\__,_/\__, /  /_/_/ /_/   \__/_/ /_/\___/   \____/\__,_/_/         
                       /____/                                                        
""")

#function for random candy in the jar
def generateCandy():
    return random.randint(50, 101)

names = []
guesses = []

print("Welcome to Guess the Candy in the Jar Game!")

candyInJar = generateCandy()

print(candyInJar)

name = ""
guess = 0

#Loop to get player input untill finished with entry
while name.lower() != 'q':
    name = input('Please Enter Your Name. Enter q to quit and view winner. ')

    if name == 'q':
        break

    names.append(name)
    guess = int(input("Enter your guess: "))
    guesses.append(guess)

winner = []
winner.append(names[0]) #deafult value set to guess at position 0
winingDistance = abs(guesses[0] - candyInJar)


for i in range(1, len(guesses)): #Loop for determining Winner.
    distance = abs(guesses[i] - candyInJar)
    if distance == winingDistance:
        winner.append(name[i])
    if distance < winingDistance:
        winner.clear()
        winingDistance = distance
        winner.append(name[i])

print("Actual number of Candy in the Jar was: ", candyInJar)

print("Winners: ", winner, f"Guesses were off by: ", winingDistance)