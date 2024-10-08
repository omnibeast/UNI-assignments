import random
import string

print("""
   ___ _           __       _   _       
  / _ (_) __ _    / /  __ _| |_(_)_ __  
 / /_)/ |/ _` |  / /  / _` | __| | '_ \ 
/ ___/| | (_| | / /__| (_| | |_| | | | |
\/    |_|\__, | \____/\__,_|\__|_|_| |_|
         |___/                          
""") #Header

# Function to remove punctuation and special characters
def clean_word(word):
    return ''.join([char for char in word if char.isalpha()])

# Function to translate word to Pig Latin
def translate(word):
    vowels = 'aeiou'
    word = clean_word(word).lower()

    if word[0] in vowels: #checking if the word begins with a vowel
        return word + 'yay'
    else:
        for i, letter in enumerate(word): #moving the first consonant cluster to the end and adding 'ay'
            if letter in vowels:
                return word[i:] + word[:i] + 'ay'.
        return word + 'ay'

def piglatin(): #Pig Latin translator main function
    while True:
        word = input("Enter a word to translate to Pig Latin (or 'quit' to exit): ")
        if word.lower() == 'quit':
            break
        print("Pig Latin Translation:",translate(word))
        print()

# Run the game
piglatin()