#Programmer: Saurav Pokharel
#Date: 08/12/2024
#Description: Program to calculate user age in different units

def main():
    #getting the frst name
    first_name = input("Please enter your first name: ")
    
    #getting last name
    last_name = input("Please enter your last name: ")
    
    #getting age input in years
    age_years = int(input("Please enter your age in years: "))
    
    #calculating age in different units
    age_months = age_years * 12
    age_days = age_years * 365  
    age_hours = age_days * 24
    age_minutes = age_hours * 60
    age_seconds = age_minutes * 60
    
    #printing the final outputs
    print(f"{last_name}, {first_name}")
    print(f"{age_years} years old.")
    print(f"{age_months} months old.")
    print(f"{age_days} days old.")
    print(f"{age_hours} hours old.")
    print(f"{age_minutes} minutes old.")
    print(f"{age_seconds} seconds old.")

main()