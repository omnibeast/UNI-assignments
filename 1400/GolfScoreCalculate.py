"""
Programer: Saurav Pokharel
Date: 10/17/2024
Description: Calculate Golf Score. 
"""
# Initialize Par and Scores List
par_values = [4, 3, 5, 4, 4, 3, 4, 5, 4]  # Default par values for 9 holes
scores = [0] * 9  # Initialize all scores to 0 (indicating no score yet)

# Function to display the main menu
def display_menu():
    print("Welcome to the Golf Score Tracker!")
    print("1. Add a score for a hole")
    print("2. Update a score")
    print("3. Delete a score")
    print("4. View all scores")
    print("5. View total score")
    print("6. Exit")

# Function to add or update a score
def add_or_update_score(update=False):
    hole = int(input("Enter hole number (1-9): "))
    if 1 <= hole <= 9:
        score = int(input("Enter score for hole " + str(hole) + ": "))
        scores[hole - 1] = score
        check_result(hole - 1)
    else:
        print("Invalid hole number.")

# Function to check result (birdie, par, etc.)
def check_result(hole):
    score = scores[hole]
    par = par_values[hole]
    if score == 0:
        print("Hole " + str(hole + 1) + ": No Score yet.")
    elif score == par:
        print("Hole " + str(hole + 1) + " is a Par " + str(par) + ". You got a Par!")
    elif score < par:
        diff = par - score
        if diff == 1:
            print("Hole " + str(hole + 1) + " is a Par " + str(par) + ". You got a Birdie!")
        elif diff == 2:
            print("Hole " + str(hole + 1) + " is a Par " + str(par) + ". You got an Eagle!")
        else:
            print("Hole " + str(hole + 1) + " is a Par " + str(par) + ". Amazing score!")
    else:
        diff = score - par
        if diff == 1:
            print("Hole " + str(hole + 1) + " is a Par " + str(par) + ". You got a Bogey!")
        else:
            print("Hole " + str(hole + 1) + " is a Par " + str(par) + ". You scored " + str(diff) + " over par.")

# Function to delete a score
def delete_score():
    hole = int(input("Enter hole number to delete score (1-9): "))
    if 1 <= hole <= 9:
        scores[hole - 1] = 0
        print("Score for hole " + str(hole) + " has been deleted.")
    else:
        print("Invalid hole number.")

# Function to view all scores
def view_scores():
    for i in range(9):
        score = scores[i]
        par = par_values[i]
        if score == 0:
            print("Hole " + str(i + 1) + ": 0 (No Score yet)")
        else:
            check_result(i)

# Function to view total score
def view_total_score():
    total = sum(scores)
    print("Total score: " + str(total))

# Function for admin access to update par values
def admin_access():
    admin = input("Enter admin password: ")
    if admin == 'golfadmin':
        print("Admin access granted: Update Par values for each hole.")
        for i in range(9):
            new_par = int(input("Enter new Par value for hole " + str(i + 1) + " (Current: " + str(par_values[i]) + "): "))
            par_values[i] = new_par
        print("Par values updated successfully!")
    else:
        print("Incorrect password!")

# Main program loop
while True:
    display_menu()
    choice = input("Enter your choice: ").lower()

    if choice == '1':
        add_or_update_score()
    elif choice == '2':
        add_or_update_score(update=True)
    elif choice == '3':
        delete_score()
    elif choice == '4':
        view_scores()
    elif choice == '5':
        view_total_score()
    elif choice == 'admin':
        admin_access()
    elif choice == '6':
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
