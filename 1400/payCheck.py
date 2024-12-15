"""
Programer: Saurav Pokharel
Date: 10/17/2024
Description: Calculate worked hours. 
"""

def checkPositiveNumericValue(hours):
    while True:
        try:
            hours = int(hours)  #check if value is a number
            if hours < 0 or hours > 80:    #check if it's between  0 and 80
                raise Exception('Value must be between  0 and 80')
            #passes the two checks
            return hours
        except ValueError:
            hours = input("Value must be number. Re-Enter: ")
        except:
            hours = input('Value must be between 0 and 80, Re-Enter: ')

name = input("Enter Employee Name: ")
hoursWorked = input("Enter Hours Worked: ")

hoursWorked = checkPositiveNumericValue(hoursWorked)

print(name + 'worked', hoursWorked, 'hours.')