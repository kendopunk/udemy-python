# hilow.py
from random import choice
import os

from art import logo, vs
from game_data import data


def descriptor(mapElement):
    return ("%s, a %s from %s" %
            (mapElement["name"], mapElement["description"], mapElement["country"]))


def comparison_statement(prefix, mapElement):
    desc = descriptor(mapElement)
    if prefix == 'A':
        print(f"Compare A: {desc}")
    if prefix == 'B':
        print(f"Against B: {desc}")


def increment_score(score):
    return score + 1


def is_correct_choice(guess, a_followers, b_followers):
    if guess == 'A' and a_followers > b_followers:
        return True
    if guess == 'B' and b_followers > a_followers:
        return True
    return False


def choose_random_entity(data):
    return choice(data)


def game():
    score = 0
    game_on = True
    a = choose_random_entity(data)
    b = choose_random_entity(data)

    while game_on:
        print(logo)
        print(f"Your score is {score}.")
        comparison_statement('A', a)
        print(vs)
        comparison_statement('B', b)

        guess = 'X'
        while not guess == 'A' and not guess == 'B':
            guess = input("Who has more followers? (A / B): ")

        if is_correct_choice(guess, a["follower_count"], b["follower_count"]):
            score = increment_score(score)
            if not guess == 'A':
                a = b
            b = choose_random_entity(data)
            os.system('clear')
        else:
            game_on = False
            print((50 * "="))
            print(f"Game over.  Your score is {score}.")
            print((50 * "="))


game()
