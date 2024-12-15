import random
 
class PigPlayer:    #class Pig defines a single person in the game
    final_goal = 50 
    score = 0
    turnTotal =0
    die =1

    def __init__(self):
        self.score = 0
        self.turnTotal = 0
        self.die = 1
    
    def roll(self):
        self.die = random.randint(1, 6) #double check this one
        self.turnTotal += self.die
        if self.die == 1:
            self.turnTotal = 0

    def stop(self):
        self.score += self.turnTotal
        self.turnTotal = 0
    
    def __str__(self):
        return  "Turn Total: " + str(self.turnTotal) + "\nScore: " + str(self.score)
 

   

print("Pig Game")

you = PigPlayer()   #instance variable for the player
computer = PigPlayer()  #instance variable for the PC
print("You", you)
while True: #game loop, keep the game going untill someone wins
    print('Your turn: ')
    
    while True: #allows the user keep rolling untill they choose to quit, or roll a 1
        #Player's turn
        choice = input('(R)oll or (S)top: ')

        #Stop if they don't choose R
        if choice != 'R' and choice != "r":
            break

        you.roll()  #calling roll function for instance variable you

        print("You Rolled: ", you.die)

        if you.die == 1:
            break

    you.stop()  #Calls the stop method for instance variable you
    print(you)  #calls __str__ function for you

    if you.score > you.final_goal:  #if you win, break out of the game loop
        break

    #Computer's turn
    print()
    print("Computer's Roll")
    while True:     #allow the computer to keep rolling
        computer.roll()
        print("Computer Rolled", computer.die)
        if computer.turnTotal < 15 and computer.die > 1 and computer.score + computer.turnTotal < 100:   #computer rolls till turn total is 15, or roll a 1, or they win
            continue
        else:
            break

    computer.stop()
    print("Computer", computer)
    if computer.score < computer.final_goal and you.score < you.final_goal:
        continue
    else:
        break

if computer.score < you.score:
    print("You Win!!")
else:
    print("Computer Wins")