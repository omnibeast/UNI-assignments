"""
Programer: Saurav Pokharel
Date: 09/02/2024
Description: Gather information about the Weber State Student and calculate the percentage of years they have been school. 
"""

print("""
 __      __        ___.                    
/  \    /  \  ____ \_ |__    ____ _______  
\   \/\/   /_/ __ \ | __ \ _/ __ \\_  __ \ 
 \        / \  ___/ | \_\ \\  ___/ |  | \/ 
  \__/\  /   \___  >|___  / \___  >|__|    
       \/        \/     \/      \/
      """)

name = input("What is your name? ")
age = int(input("What is your age? "))
yearinschool = int(input("How many years of school: "))
percentinschool = round(yearinschool / age * 100)
print("You have spent", percentinschool, "percent of your life in school")