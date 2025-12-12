#This is the progarm of Hangman game.
#In hangman game you should guess the letters of word until the word is completed. If you enter the wrong letter six times you will lose.

#Mahdi Hussaini

import random
print("Welcome to hangman game")
words = ["night", "window", "recycle", "letter", "information", "earthquake", "galaxy", "represent", "mother", "electricity"]
stages = [
    """
      +---+
      |   |
          |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
          |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
      |   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|   |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
          |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     /    |
          |
    =========
    """,
    """
      +---+
      |   |
      O   |
     /|\\  |
     / \\  |
          |
    =========
    """
]
ran_word = words[random.randint(0, len(words)-1)]
guessed = []


for i in ran_word:
    print("_", end='')
    guessed.append("_")

life = 0
while life < 6:
    counter = 0
    life_counter = True
    match = ""
    guess_letter = (input("\nGuess the letter: ")).lower()
    for i in ran_word:
        if guess_letter == i:
            guessed[counter] = i
            life_counter = False
        counter += 1
    if life_counter:
        life += 1
        if life != 6:
            print(f"wrong letter!")
    print(stages[life])
    if life != 6:
        for i in guessed:
            print(i, end="")
            match += i
        if match == ran_word:
            print(f"\n\n**********YOU WON**********")
            break
    if life == 6:
        print("**********YOU LOST!**********")