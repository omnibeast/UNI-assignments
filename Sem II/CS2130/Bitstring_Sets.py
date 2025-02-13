# Saurav Pokharel
# CS2130

def get_bitstring_from_set(set_input): 
    bitstring = 0
    for element in set_input:
        bitstring |= (1 << element) # sets the bit corresponding to the elements
    return bitstring

def set_bitstring(bitstring):
    return {i for i in range(10) if bitstring & (1 << i)}   # Extract elements from the bitstring

def complement(bitstring):
    return ~bitstring & 0b1111111111    # Flips the bits and mask to retain only 10 bits

def union(bitstring_a, bitstring_b):
    return bitstring_a | bitstring_b    # OR operation to get the union

def intersection(bitstring_a, bitstring_b):
    return bitstring_a & bitstring_b    # AND operation to get the intersection

def difference(bitstring_a, bitstring_b):
    return bitstring_a & ~bitstring_b   # AND operation with the complement of B to get the difference

def symmetric_difference(bitstring_a, bitstring_b):
    return bitstring_a ^ bitstring_b    # XOR operation to get the symmetric difference

def input_set():
    while True:
        try:
            num_elements = int(input("Enter number of element in Set: "))
            if num_elements < 0 or num_elements > 10:   
                
                raise ValueError("Elemented must be between 0-10")
           
            elements = set()
            for i in range(num_elements):
                while True:
                    try:
                        element = int(input(f"Enter element {i + 1}: "))
                        if element < 0 or element > 9:
                            raise ValueError("Element must be between 0-9")

                        elements.add(element)
                        break
                    except ValueError as e:
                        print(e)
            return elements
        except ValueError as e:
            print(e)

print(r"""
 _______  _______  _______  __    ______   _______ 
(  ____ \(  ____ \/ ___   )/  \  / ___  \ (  __   )
| (    \/| (    \/\/   )  |\/) ) \/   \  \| (  )  |
| |      | (_____     /   )  | |    ___) /| | /   |
| |      (_____  )  _/   /   | |   (___ ( | (/ /) |
| |            ) | /   _/    | |       ) \|   / | |
| (____/\/\____) |(   (__/\__) (_/\___/  /|  (__) |
(_______/\_______)\_______/\____/\______/ (_______)
                                                   
                                                   
Computational Structure | Saurav Pokharel""")
print("This program reads in the values of two sets and \ndisplays the result of different operations on the sets.")
print("\n Enter Set A ")
set_a = input_set()
print("\n Enter Set B: ")
set_b = input_set()

bitstring_a = get_bitstring_from_set(set_a)
bitstring_b = get_bitstring_from_set(set_b)

print("\nResults: ")
print(f"Set A = {set_a}")
print(f"Set B = {set_b}")
print(f"Compement of A = {set_bitstring(complement(bitstring_a))}")
print(f"Union of A and B = {set_bitstring(union(bitstring_a, bitstring_b))}")
print(f"Intersection of A and B = {set_bitstring(intersection(bitstring_a, bitstring_b))}")
print(f"Difference of A and B = {set_bitstring(difference(bitstring_a, bitstring_b))}")
print(f"Symmetric difference of A and B = {set_bitstring(symmetric_difference(bitstring_a, bitstring_b))}")

