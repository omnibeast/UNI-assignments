
# Programer: Saurav Pokharel
# Date: 09/19/2024
# Description:Zoo Cost Estimator

print("""
  _  __                                         _____              ____          _     _____     _   _                 _             
 | |/ /__ _ _ __   __ _  __ _ _ __ ___   ___   |__  /___   ___    / ___|___  ___| |_  | ____|___| |_(_)_ __ ___   __ _| |_ ___  _ __ 
 | ' // _` | '_ \ / _` |/ _` | '__/ _ \ / _ \    / // _ \ / _ \  | |   / _ \/ __| __| |  _| / __| __| | '_ ` _ \ / _` | __/ _ \| '__|
 | . | (_| | | | | (_| | (_| | | | (_) | (_) |  / /| (_) | (_) | | |__| (_) \__ | |_  | |___\__ | |_| | | | | | | (_| | || (_) | |   
 |_|\_\__,_|_| |_|\__, |\__,_|_|  \___/ \___/  /____\___/ \___/   \____\___/|___/\__| |_____|___/\__|_|_| |_| |_|\__,_|\__\___/|_|   
                  |___/                                                                                                              
""")

print('Welcome to the Kangaroo Zoo Cost Estimator') 

while True: #sets while loop to true for infinite loop.
    print('Choose an option:')
    print('1. Estimate Cost')
    print('2. Quit')


    choice = input('Enter Choice:')

    if choice == "1":
        guest_below_3 = int(input("How many guests are 3 and below? ")) #geting number of guest below 3
        guest_other = int(input("How many other guest will be jumping? ")) #geting number of other guest.
        passes = input('Do you want to buy any flopper passes?(y/n) ') #asks if user wants to buy flopper passes

        cost = 0 #sets initial costs to 0

        cost += guest_below_3 * 6 #calculate cost for guest below 3
        cost += guest_other * 12 #calculate cost for other guest

        if passes.lower() == "y": #if user wants flopper pass runs following code 
            
            guest_below_3 = int(input('How many passes for 3 and below? ')) #gets number of passes for guest below 
            regular_pass = int(input('How many regular passes?')) #gets number of passes for other user

            cost += guest_below_3 * 50 #calculate cost for flopper passes for guest bleow 3 
            cost += regular_pass * 85 #calculate cost for flopper passes for other guest 

        print("Cost Estimation: USD", cost) #prints estimated cost

    elif choice == "2": 
        print('Thanks for using the Kangaroo Zoo Cost Estimator!')
        break

    else:
        print('Invalid choice. Please try again.') #prints error msg if user input character other than 1 and 2