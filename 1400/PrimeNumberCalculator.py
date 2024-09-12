"""
Programer: Saurav Pokharel
Date: 09/11/2024
Description: Prints out whether the user input number is prime number or not.
"""
print("""
___  ____ _ _  _ ____    _  _ _  _ _  _ ___  ____ ____    ____ _  _ ____ ____ _  _ ____ ____ 
|__] |__/ | |\/| |___    |\ | |  | |\/| |__] |___ |__/    |    |__| |___ |    |_/  |___ |__/ 
|    |  \ | |  | |___    | \| |__| |  | |__] |___ |  \    |___ |  | |___ |___ | \_ |___ |  \ 
                                                                                             
""")

number = 0
while number != -1:    
    number = int(input("Enter a positive number(Enter -1 to quit.) :")) #Getting the user input
    if number == -1:
        break #breaking loop
    if number < -1:
        print("Must enter positive a number.")
        continue #starting of next iteration

    Prime = True #Sets the default boolen value for Prime to True
    for i in range(2, number):
        if number % i == 0:
            Prime = False
            break #breaking loop

    if Prime:
        print(number, "is a prime number.")
    else:
        print(number, "is not a prime number.")

print("Thank you for using Prime number checker.")