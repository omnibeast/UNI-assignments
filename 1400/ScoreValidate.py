"""
Programer: Saurav Pokharel
Date: 11/01/2024
Description: Quiz Score Validate. 
"""

print("""
   ____        _        _____                     __      __   _ _     _       _       
  / __ \      (_)      / ____|                    \ \    / /  | (_)   | |     | |      
 | |  | |_   _ _ ____ | (___   ___ ___  _ __ ___   \ \  / /_ _| |_  __| | __ _| |_ ___ 
 | |  | | | | | |_  /  \___ \ / __/ _ \| '__/ _ \   \ \/ / _` | | |/ _` |/ _` | __/ _ 
 | |__| | |_| | |/ /   ____) | (_| (_) | | |  __/    \  / (_| | | | (_| | (_| | ||  __/
  \___\_\\__,_|_/___| |_____/ \___\___/|_|  \___|     \/ \__,_|_|_|\__,_|\__,_|\__\___|
                                                                                       
                                                                                       
""")

def get_valid_score(): #function to get score from user with exception
    while True:
        try:
            score = input("Enter a score: ")
            score = float(score)
            if score < 0 or score > 100: 
                print("Sorry, the score must be between 0 and 100.")
            else:
                return score
        except ValueError:
            print("Sorry, the score must be a number.")

def calculate_stats(scores): #function to calculate and print highest, lowest and average scores
    if scores:
        highest = max(scores)
        lowest = min(scores)
        average = sum(scores) / len(scores)
        print("High:", highest)
        print("Low:", lowest)
        print("Average:", round(average, 2))
        print("Number of Students:", len(scores))
    else:
        print("No scores to calculate.")

def main(): #main function
    scores = [] #creating empty list of score to begin with
    while True:
        scores.append(get_valid_score()) #adding score to list
        choice = input("Press 's' to enter another score or 'c' to calculate: ").lower()
        if choice == 'c':
            calculate_stats(scores)
            break

main() #runing the main function
