"""
Programer: Saurav Pokharel
Date: 09/12/2024
Description: Checks the strength of Password based on user input. 
"""

print("""╔═╗┌─┐┌─┐┌─┐┬ ┬┌─┐┬─┐┌┬┐  ╔═╗┌┬┐┬─┐┌─┐┌┐┌┌─┐┌┬┐┬ ┬  ╔═╗┬ ┬┌─┐┌─┐┬┌─
╠═╝├─┤└─┐└─┐││││ │├┬┘ ││  ╚═╗ │ ├┬┘├┤ ││││ ┬ │ ├─┤  ║  ├─┤├┤ │  ├┴┐
╩  ┴ ┴└─┘└─┘└┴┘└─┘┴└──┴┘  ╚═╝ ┴ ┴└─└─┘┘└┘└─┘ ┴ ┴ ┴  ╚═╝┴ ┴└─┘└─┘┴ ┴ """)

#Set the initial value  of score to 0
score = 0

print("Answer the following question to know your password strength.")

#Getting the user input and incrementing score 
answer1 = input("Does your password contain at least 9 characters in length? (y or n): ")
if answer1 == "y" or answer1 == "Y":
  score += 1 #Increases the password score by 1 if user input Y or y in question 1

answer2 = input("Does your password contain letters and numbers? (y or n): ")
if answer2 == "y" or answer2 == "Y":
  score += 1 #Increases the password score by 1 if user input Y or y in question 2

answer3 = input("Does your password contain a mixture of upper and lower case letters? (y or n): ")
if answer3 == "y" or answer3 == "Y":
  score += 1 #Increases the password score by 1 if user input Y or y in question 3

answer4 = input("Does your password contain at least one symbol? (y or n): ")
if answer4 == "y" or answer4 == "Y":
  score += 1 #Increases the password score by 1 if user input Y or y in question 4

# Determine password strength comparing the score.
if score <= 1: 
  print("Your password is considered very weak.")
elif score == 2:
  print("Your password is considered weak.")
elif score == 3:
  print("Your password is considered strong.")
else:
  print("Your password is considered very strong.")

print("Thank you for using Password strength checker.") 