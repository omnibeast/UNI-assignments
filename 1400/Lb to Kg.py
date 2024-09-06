#ASCII Art of Program Name
print("""
┓ ┓       ┓     ┏┓┏┓┳┓┓┏┏┓┳┓┏┳┓┏┓┳┓
┃ ┣┓  ━━  ┃┏┏┓  ┃ ┃┃┃┃┃┃┣ ┣┫ ┃ ┣ ┣┫
┗┛┗┛      ┛┗┗┫  ┗┛┗┛┛┗┗┛┗┛┛┗ ┻ ┗┛┛┗
             ┛                                                                    
""")

#Printing welcome message.
print('Welcome to Pound to Kilogram weight converter.')

#Program type selection
type = input('Type 1 for Lb-Kg else type 2 for Kg-Lb: ')

#Code to run if user input is 1.
if type == '1':
    lb = float(input('Enter the weight in Lb: '))
    kg = lb * 0.45359237
    print(lb,  'Pound is', kg, 'Kilogram')

#Code to run if user input is 2.
elif type == '2':
    kg = int(input('Enter the weight in Kg: '))
    lb = kg / 2.20462262
    print(kg, 'Kilogram is', lb,'Pound')

#printing the error message if the user input other than 1 or 2 while selecting program type
else:
    print('Invalid choice. Please restart the program and enter 1 or 2.')

#Printing the thank you message
print('Thank you for using Lb-Kg weight conveter.')