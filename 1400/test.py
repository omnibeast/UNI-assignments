# Police Speed app
import math

d = float(input("Enter the length of the skidmark on the pavement"))
v = 0               #Modify the variable to code the equation

d3times = 3 * d
v = math.sqrt(d3times)
v = round(d, 2)
print("Speed of the car:", v)
