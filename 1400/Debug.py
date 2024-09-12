#Keeps track of the amount of prime numbers the user enters
num = int(input("Enter a positive value: -1 to quit "))
evenCount = 0
isEven = True
while num > 0:
  if num % 2 != 0:
    isEven = False
  if isEven:
    print(num, "is even")
    evenCount += 1
  else:
    print(num, "is odd")
  num = int(input("Enter a positive value: -1 to quit "))

print("Even Count: ", evenCount)