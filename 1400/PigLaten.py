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
    """Remove punctuation and special characters from a word."""
    return ''.join([char for char in word if char.isalpha()])


# Function to translate word to Pig Latin
def translate(word):
    """Translate a word to Pig Latin."""
    vowels = 'aeiou'
    word = clean_word(word).lower()

    if word[0] in vowels: #checking if the word begins with a vowel
        return word + 'yay'
    else:
        for i, letter in enumerate(word): #moving the first consonant cluster to the end and adding 'ay'
            if letter in vowels:
                return word[i:] + word[:i] + 'ay'
        return word + 'ay'


def piglatin(): #Pig Latin translator main function
    print("Welcome to the Pig Latin Translator!")
    while True:
        sentence = input("Enter a sentence to translate (or 'quit' to exit): ")
        if sentence.lower() == 'quit':
            break
        
        # Split sentence into words, translate each word, and join back into sentence
        translated_sentence = ' '.join([translate(word) for word in sentence.split()])
        
        print("Sentence translated to Pig Latin:", translated_sentence)
        print()


# Run the game
piglatin()
