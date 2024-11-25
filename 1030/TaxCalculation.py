"""
Programer: Saurav Pokharel
Date: 11/23/2024
Description: Calculates the total taxes of give bill amount ie food bill 150 & non food bill 50. 
"""

#SalesTaxRate
foodTax = 3 / 100
nonFoodTax = 6.75 /100

#Bills
foodBill = 150
nonFoodBill = 50

#taxCalculation
totalTax = foodBill * foodTax + nonFoodBill * nonFoodTax

# Output the result
print(f"The total tax for your bill is: {totalTax:}")
print(f"Total Bill including tax is: {foodBill + nonFoodBill + totalTax}")