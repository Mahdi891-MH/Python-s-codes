import random

rand_number = random.randint(1, 100)
correct = False


def check(number, guessed):
    if guessed > number:
        return "Too high \nguess again"
    elif guessed < number:
        return "Too low\nguess again"
    elif number == guessed:
        global correct
        correct = True
        return "Your guess is correct\n\n*****YOU WIN*****"


def difficulty_level(diff):
    attempt = 0
    if diff == "hard":
        attempt = 5
    if diff == "easy":
        attempt = 10
    return attempt


while True:
    print("Welcome to guessing number game\nI'm thinking of a number between 1 and 100")
    difficulty = input("Choose the difficulty. Type 'easy' or 'hard': ").lower()
    user_attempts = difficulty_level(difficulty)
    while user_attempts > 0:
        print(f"You have got {user_attempts} attempts")
        user_guess = int(input("Make a guess: "))
        print(check(rand_number, user_guess))
        if correct:
            break
        user_attempts -= 1
        if user_attempts == 0:
            print("\n*****YOU LOSE!*****")
    again = input("Do you want to play again type 'y' for yes and 'n' for no: ").lower()
    if again == 'n':
        break