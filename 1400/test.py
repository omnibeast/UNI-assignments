# Kangaroo Zoo Cost Estimator

print("Welcome to the Kangaroo Zoo Cost Estimator")

while True:
    print("\nChoose an option:")
    print("1. Estimate Cost")
    print("2. Quit")

    choice = input("Enter choice: ")

    if choice == "1":
        # Get number of guests 3 and under
        num_under_3 = int(input("How many guests are 3 and under? "))

        # Get number of other guests
        num_other_guests = int(input("How many other guests will be jumping? "))

        # Ask if user wants to buy flopper passes
        buy_passes = input("Do you want to buy any flopper passes? (yes/no) ")

        # Initialize cost
        cost = 0

        # Calculate cost for guests 3 and under
        cost += num_under_3 * 6

        # Calculate cost for other guests
        cost += num_other_guests * 12

        # If user wants to buy flopper passes
        if buy_passes.lower() == "yes":
            # Get number of passes for 3 and under
            num_under_3_passes = int(input("How many passes for 3 and under? "))

            # Get number of regular passes
            num_regular_passes = int(input("How many regular passes? "))

            # Calculate cost for flopper passes
            cost += num_under_3_passes * 50
            cost += num_regular_passes * 85

        # Print cost estimation
        print(f"Cost Estimation: ${cost}")

    elif choice == "2":
        print("Thanks for using the cost estimator!")
        break
    else:
        print("Invalid choice. Please try again.")
