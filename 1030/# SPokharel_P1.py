# SPokharel_P1.py

# Function to calculate grades and letter grades
def calculate_grade():
    while True:
        # Get student information
        student_id = input("Enter Student ID: ")
        first_name = input("Enter First Name: ")
        last_name = input("Enter Last Name: ")

        # Get scores for each category
        try:
            assignments = float(input("Enter Assignments Score (0-100): "))
            quizzes = float(input("Enter Quizzes Score (0-100): "))
            midterm = float(input("Enter Midterm Exam Score (0-100): "))
            final_exam = float(input("Enter Final Exam Score (0-100): "))
        except ValueError:
            print("Invalid input! Please enter numbers only.")
            continue  # Restart if input is invalid

        # Check if scores are within the valid range
        if not (0 <= assignments <= 100 and 0 <= quizzes <= 100 and 0 <= midterm <= 100 and 0 <= final_exam <= 100):
            print("All scores must be between 0 and 100.")
            continue

        # Calculate total score
        total_score = (assignments * 0.50) + (quizzes * 0.20) + (midterm * 0.10) + (final_exam * 0.20)

        # Determine letter grade
        if total_score >= 90:
            letter_grade = 'A'
        elif total_score >= 80:
            letter_grade = 'B'
        elif total_score >= 70:
            letter_grade = 'C'
        elif total_score >= 60:
            letter_grade = 'D'
        else:
            letter_grade = 'E'

        # Print results
        print("\n" + last_name + ", " + first_name)
        print("Student ID: " + student_id)
        print("Homework: " + str(assignments))
        print("Quizzes: " + str(quizzes))
        print("Midterm: " + str(midterm))
        print("Final: " + str(final_exam))
        print("Total Score: " + str(round(total_score, 2)) + "     Grade: " + letter_grade)

        # Ask if the user wants to enter another student
        repeat = input("\nDo you want to enter another student? (yes/no): ").lower()
        if repeat != 'yes':
            print("Goodbye!")
            break  # Exit the loop if the user doesn't want to continue

# Run the program
calculate_grade()
