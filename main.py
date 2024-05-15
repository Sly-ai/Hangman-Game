import os
import random
import time

# Function to clear screen
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

print("Play Hangman")
print()
MAX_CHANCES = 6
list_of_words = [
    "horse",
    "brazzers",
    "python",
    "sunshine",
    "battery",
    "binance",
    "london",
    "sofa",
    "kidney",
    "land",
]

tries = []
word = random.choice(list_of_words)
chances = MAX_CHANCES  # Initialize chances

# Function to draw Hangman ASCII art
def draw_hangman(chances):
    HANGMANPICS = ['''
      +---+
      |   |
          |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
          |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
          |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     /    |
          |
    =========''', '''
      +---+
      |   |
      O   |
     /|\  |
     / \  |
          |
    =========''']
    return HANGMANPICS[MAX_CHANCES - chances]

while True:
    time.sleep(1)
    clear_screen()
    print(draw_hangman(chances))
    print()
    letter = input("Input a letter > ").lower()
    if len(letter) != 1 or not letter.isalpha():
        print("Please enter a single letter.")
        continue
    if letter in tries:
        print("You've tried that before.")
        continue
    tries.append(letter)
    if letter in word:
        print("You found a letter.")
    else:
        print("Try again.")
        chances -= 1
        print(f"You have {chances} chances left!")

    all_letters = True
    print()
    for char in word:
        if char in tries:
            print(char, end="")
        else:
            print("_", end="")
            all_letters = False

    if all_letters:
        print(f"\nYou've won with {chances} chances left!")
        break
    if chances == 0:
        print("Game over! You have run out of chances.")
        break
