A = [1, 3, 5, 7, 8, 9, 10]
B = [2, 4, 6, 7, 9]

union = []
for number in A:
        union.append(number)

for number in B:
    if number not in union:
        union.append(number)   

intersection = []
for number in A:
    if number in B:
        intersection.append(number)

difference = []
for number in A:
    if number not in B:
        difference.append(number)

print("A U B =", union)
print("A ∩ B =", intersection)
print("A - B =", difference)