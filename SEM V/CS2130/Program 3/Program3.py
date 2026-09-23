#Getting the starting count from the user
start_count = int(input("Enter the starting count: (Enter 5 to get the exaact sequence in assignment) 5"))

#storing the generated sequence in a variable
sequence = ""

#decrease the count after each group of letters
for count in range(start_count, 0, -1):
    for repetition in range(count): #add the required number of "a"s
        sequence += "a"
    for repetition in range(count): #add the required number of "b"s
        sequence += "b"

print("Generated Sequence:", sequence) #just printing the generated sequence

