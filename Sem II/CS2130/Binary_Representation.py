# Saurav Pokharel
# Program to represent

def print_binary(value):
    """
    Prints the binary representation of an integer.
    """
    binary_representation = ""
    for i in range(31, -1, -1):  # Loop from the most significant bit to the least significant bit
        if (value >> i) & 1:  # Check if the bit at position i is 1
            binary_representation += "1 "
        else:  # Otherwise, the bit is 0
            binary_representation += "0 "
        # Add spacing every 4 bits for readability
        if i % 4 == 0 and i != 0:
            binary_representation += "  "
    print(binary_representation)

def main():
    print("""
  _____       _                             _          ____  _                        
 |_   _|     | |                           | |        |  _ \(_)                       
   | |  _ __ | |_ ___ _ __ __ _  ___ _ __  | |_ ___   | |_) |_ _ __   __ _ _ __ _   _ 
   | | | '_ \| __/ _ \ '__/ _` |/ _ \ '__| | __/ _ \  |  _ <| | '_ \ / _` | '__| | | |
  _| |_| | | | ||  __/ | | (_| |  __/ |    | || (_) | | |_) | | | | | (_| | |  | |_| |
 |_____|_| |_|\__\___|_|  \__, |\___|_|     \__\___/  |____/|_|_| |_|\__,_|_|   \__, |
                           __/ |                                                 __/ |
                          |___/                                                 |___/ 
""")

    while True:
        try:
            number = int(input("\nPlease enter an integer to display its binary representation (0 to quit): "))
            if number == 0:
                break  # Exit the loop if the user enters 0

            print(f"The binary representation of {number} is:")
            print_binary(number)
        except ValueError:
            print("Invalid input. Please enter a valid integer.")

    print("\nThanks! Have a great day!")

if __name__ == "__main__":
    main()
