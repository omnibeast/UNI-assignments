#Programmer: Saurav Pokharel
#Date: 25/11/2024
#Description: Program to calculate students score and letter grades

print("""                                                        
 _____           _ _            _____         _             
|   __|___ ___ _| |_|___ ___   |   __|_ _ ___| |_ ___ _____ 
|  |  |  _| .'| . | |   | . |  |__   | | |_ -|  _| -_|     |
|_____|_| |__,|___|_|_|_|_  |  |_____|_  |___|_| |___|_|_|_|
                        |___|        |___|by Saurav Pokharel             
""")

def calc_grade():
    while True:
        #student information collection
        id_student = input("Student ID: ")
        name_first = input("First Name: ")
        name_last = input("Last Name: ")

        try:
            #score collection
            score_assignments = float(input("Enter Score for Assugnments (0-100):"))
            score_quizzes = float(input("Enter Score for Quizzes (0-100):"))
            score_midterm = float(input("Enter Score for Midterm (0-100):"))
            score_final = float(input("Enter Score for Final Exam (0-100):"))   
        except ValueError:
            print("Error: Invalid input. \n Please enter values between 0 and 100")
        #checking if the score are valid
        
        if not (0 <= score_assignments <= 100 and 0 <= score_quizzes <= 100 and 0 <= score_midterm <= 100 and 0 <= score_final <= 100):
            print("Scores must be between 0 to 100.")
            continue

        #total score calculation
        score_total = (score_assignments * 0.50 + score_quizzes * 0.20 + score_midterm * 0.10 + score_final * 0.20)

        #letter grade system
        if score_total >= 90:
            grade = "A"
        elif score_total >= 80:
            grade = "B"
        elif score_total >= 70:
            grade = "B"
        elif score_total >= 60:
            grade = "B"
        else:
            grade = "E"

        #Printing all the data
        print(f"\n{name_first}, {name_last}")
        print(f"Student ID: {id_student}")
        print(f"Homework: {score_assignments}")
        print(f"Quizzes: {score_quizzes}")
        print(f"Midterm: {score_midterm}")
        print(f"Final: {score_final}")
        print(f"Total Score: {score_total:.2f},  Grade: {grade}")

        #getting user input either to enter another student.
        addStudent = input("Would you like to enter another student? (y/n): ").lower()
        if addStudent != "y":
            print("Thank you for using the grade calculator")
            break   #exiting the loop

calc_grade() #run the program