"""
Programer: Saurav Pokharel
Date: 09/24/2024
Description: Palindrome Tester. 
"""
#Function that prints a header.
def printHead(text):
    line ="---------------------------"
    print(line)
    print('>', text)
    print(line)

#Clean a string, remove spaces, and punctuation and lowercase
def clean(phrase):
    letters = "abcdefghijklmnopqrstuvwxyz"
    cleanString = ""
    for i in phrase.lower():
        if i in letters:
            cleanString += i
    return cleanString


#determine if a phrase is palindrom or not
def isPal (phrase):
    cleanString = clean(phrase)
    backwards = cleanString[::-1]
    if cleanString == backwards:
        return True
    return False

#main program
printHead("Palindrome Tester")

phrase = ""
while phrase != "q":
    phrase = input("Enter a phrase or (q)uit: ")
    if phrase.lower() == "q" or phrase.lower() =="quit":
        break
    if isPal(phrase):
        print(phrase, "is a Palindrome.")
    else:
        print(phrase, "is not a Palindrome.")