"""
Programer: Saurav Pokharel
Date: 09/17/2024
Description: Pythagorean Theorem program that accepts inputs of the two sides of the triangle and displays the third side.
"""
import math #importing math library

#getting user input for side A and side B
sideA = float(input('Enter in side A '))
sideB = float(input('Enter in side B '))

#squaring side A and side B
sideAsquared = math.pow(sideA, 2)
sideBsquared = math.pow(sideB, 2)

#adding squared side A and B to get squared C and they doing squareroot using function math.sqrt to get side C
sideCsquared = sideAsquared + sideBsquared
sideC = math.sqrt(sideCsquared)

#printing side C
print('Side C:', sideC)