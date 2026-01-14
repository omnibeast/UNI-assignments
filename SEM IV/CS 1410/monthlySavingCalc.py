#creating a function to check the numeric input.(Error Handeling) Ref. https://www.w3schools.com/python/python_try_except.asp
def numeric_check(check):
    while True:         #creating infinte loop to keep asking until valid input is given
       try: 
           value = float(input(check))      #asking user for input and converting it to number
           return value                     #return the valid number and exit the loop
       except ValueError:                   #if input is not valid number, catch the error  and print error
           print("Error: Please enter a valid number. \n")

#just an intro
print(r"""
  __  __             _   _     _         ____            _            _      _____      _ 
 |  \/  |           | | | |   | |       |  _ \          | |          | |    / ____|    | |
 | \  / | ___  _ __ | |_| |__ | |_   _  | |_) |_   _  __| | __ _  ___| |_  | |     __ _| |
 | |\/| |/ _ \| '_ \| __| '_ \| | | | | |  _ <| | | |/ _` |/ _` |/ _ \ __| | |    / _` | |
 | |  | | (_) | | | | |_| | | | | |_| | | |_) | |_| | (_| | (_| |  __/ |_  | |___| (_| | |
 |_|  |_|\___/|_| |_|\__|_| |_|_|\__, | |____/ \__,_|\__,_|\__, |\___|\__|  \_____\__,_|_|
                                  __/ |                     __/ |                         
                                 |___/                     |___/                          """)

#getting user inout
name = input("Enter your name: ")
monthly_income =  numeric_check("Enter your monthly income: ")
monthly_rent = numeric_check("Enter your monthly rent or mortgage: ")
monthly_food_expenses = numeric_check("Enter your food expenses: ")
monthly_transportation_expenses = numeric_check("Enter your transportation expenses: ")

#calculating the expenses and savings
monthly_expense = float(monthly_rent) + float(monthly_food_expenses) + float(monthly_transportation_expenses)
savings = float(monthly_income) - monthly_expense

#calculating savings percentage with error handling for zero or negative income
if monthly_income > 0:
    savings_percentage = (savings / float(monthly_income)) * 100
else:
   savings_percentage = 0
   print("Monthly income is zero or negative, cannot calculate savings percentage.")

#printing the data
print("\n--- Monthly Budget Summary for", name, "---")
print(f"Total Monthly Income: ${monthly_income}")
print(f"Total Monthly Expenses: ${monthly_expense}")
print(f"Total Monthly Savings: ${savings}")
print(f"Savings Percentage: {savings_percentage:.2f}%") #formatting to 2 decimal places
print(f"Thank you, {name}, for using the Monthly Budget Calculator!")
 