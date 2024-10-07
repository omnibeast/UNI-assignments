import random
import string

# Function to remove punctuation and special characters
def clean_word(word):
    return ''.join([char for char in word if char.isalpha()])

# Function to translate word to Pig Latin
def pig_latin_translate(word):
    vowels = 'aeiou'
    word = clean_word(word).lower()

    # Check if the word starts with a vowel
    if word[0] in vowels:
        return word + 'yay'
    else:
        # Move the first consonant cluster to the end and add 'ay'
        for i, letter in enumerate(word):
            if letter in vowels:
                return word[i:] + word[:i] + 'ay'
        # If no vowels found (in rare cases), just return the word with 'ay'
        return word + 'ay'

# Main function to run the Pig Latin translator
def pig_latin_game():
    while True:
        word = input("Enter a word to translate to Pig Latin (or 'quit' to exit): ")
        if word.lower() == 'quit':
            break
        print(f"Pig Latin Translation: {pig_latin_translate(word)}")
        print()

# Run the game
pig_latin_game()