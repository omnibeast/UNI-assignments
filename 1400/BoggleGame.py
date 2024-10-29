"""
Programer: Saurav Pokharel
Date: 10/17/2024
Description: Boogle Game. 
"""

import random

print("""
  ____                    _                                   
 |  _ \                  | |                                  
 | |_) | ___   __ _  __ _| | ___    __ _  __ _ _ __ ___   ___ 
 |  _ < / _ \ / _` |/ _` | |/ _ \  / _` |/ _` | '_ ` _ \ / _ \
 | |_) | (_) | (_| | (_| | |  __/ | (_| | (_| | | | | | |  __/
 |____/ \___/ \__, |\__, |_|\___|  \__, |\__,_|_| |_| |_|\___|
               __/ | __/ |          __/ |                     
              |___/ |___/          |___/                      
""")

#Dictionary for points per letter
letter_points = {
    'A': 1, 'B': 3, 'C': 3, 'D': 2, 'E': 1,
    'F': 4, 'G': 2, 'H': 4, 'I': 1, 'J': 8,
    'K': 5, 'L': 1, 'M': 3, 'N': 1, 'O': 1,
    'P': 3, 'Q': 10, 'R': 1, 'S': 1, 'T': 1,
    'U': 1, 'V': 4, 'W': 4, 'X': 8, 'Y': 4, 'Z': 10
}

#Function to generate a random Boggle board
def generate_board():
    board = []
    for _ in range(5):
        row = [chr(random.randint(65, 90)) for _ in range(5)]  #65 is 'A', 90 is 'Z'
        board.append(row)
    return board

#Function to display the Boggle board
def display_board(board):
    for row in board:
        print('  '.join(row))

#Function to calculate score for a word
def calculate_word_score(word):
    return sum(letter_points.get(letter.upper(), 0) for letter in word)

#Main Boggle game function
def play_boggle():
    board = generate_board()
    print("Boggle Board:")
    display_board(board)

    total_score = 0
    while True:
        word = input("Enter a word (q to quit): ").strip()
        if word.lower() == 'q':
            break

        score = calculate_word_score(word)
        total_score += score
        print(f"Score: {total_score}")

    print("Thank you for playing!")

#Start the Boggle game
play_boggle()
