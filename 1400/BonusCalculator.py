"""
Programer: Saurav Pokharel
Date: 09/03/2024
Description: Calculates the employee bonuses based on their rating and service year.
"""
# Ask the user for their performance rating and years of service.
rate = float(input("Enter your performance rating (0-5): "))
years = int(input("How many year have you serviced for: "))

# Calculate the bonus based on the performance rating and years of service
if rate < 3:
    bonus = 0
    print("No bonus this year. You need peformance improvement.")
elif rate >= 3 and years < 2:
    bonus = 500
    print("You're awarded a bonus of USD", bonus, "for your performance!")
elif rate >= 3 and years >= 2:
    bonus = 1000
    print(f"You're awarded a bonus of USD", bonus, "for your consistent performance!")
else:
    print("Invalid input, please enter correct values.")

print("Thank you for using bonus calculator.")
