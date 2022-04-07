# Welcome to the Number Guessing Game!
# I'm thinking of a number between 1 and 100
# Choose a difficulty (e = easy / h = hard)

import random

TURNS_EASY_LEVEL = 10
TURNS_HARD_LEVEL = 5
MAX_NUM = 100

domain = range(1, MAX_NUM + 1)
answer = random.choice(domain)
difficulty = ''
game_on = True
spot_on = False


def max_tries(difficulty):
    if difficulty == 'h':
        return TURNS_HARD_LEVEL
    return TURNS_EASY_LEVEL


def end_game():
    global game_on
    game_on = False


def process_guess(guess, attempts):
    if guess > answer:
        print("Too high.")
        print(f"You have {attempts - 1} tries left.")
        if attempts - 1 == 0:
            return (attempts - 1, False, False)
        else:
            return (attempts - 1, True, False)
    elif guess < answer:
        print("Too low.")
        print(f"You have {attempts - 1} tries left.")
        if attempts - 1 == 0:
            return (attempts - 1, False, False)
        else:
            return (attempts - 1, True, False)
    else:
        print(f"You guessed the correct number of {answer}.")
        return (attempts - 1, False, True)


print("Welcome to the Number Guessing Game!")
print(f"I'm thinking of a number between 1 and {MAX_NUM}, inclusive.")
while not difficulty == 'e' and not difficulty == 'h':
    difficulty = input("Choose a difficulty (e = easy / h = hard): ")
    tries = max_tries(difficulty)
    print(f"You have {tries} attempts to get the correct answer.")

attempts = tries

while game_on and attempts > 0:
    guess = int(input("Make a guess: "))
    (attempts, game_on, spot_on) = process_guess(guess, attempts)

if not game_on and not spot_on and attempts == 0:
    print(f"Game over, you lose.  The answer was {answer}")
