##############################
# day11/blackjack.py
# modification...ace can be 11 or 1
##############################
import os
import random

card_values = {
    "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11
}


def new_deck():
    return [
        '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
        '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9',
        '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q',
        'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']


def get_card(deck):
    card = random.choice(deck)
    return card


def is_blackjack(cards):
    return len(cards) == 2 and cards.count('A') == 1 and (
        cards.count('10') == 1 or cards.count(
            'J') == 1 or cards.count('Q') == 1 or cards.count('K') == 1
    )


def calculate_hand_value(cards):
    if is_blackjack(cards):
        return 100

    else:
        sum = 0
        for card in cards:
            sum += card_values[card]

        num_aces = cards.count('A')
        if num_aces > 0 and sum > 21:
            while sum > 21:
                sum -= 10

        return sum


def remove_from_deck(deck, value):
    deck.remove(value)
    return deck


def show_your_cards(cards):
    print(f"Your cards: {cards} = {calculate_hand_value(cards)}")


def show_dealer_cards(cards):
    print(f"Dealer cards: {cards} = {calculate_hand_value(cards)}")


def compare_hand(y, d):
    yv = calculate_hand_value(y)
    dv = calculate_hand_value(d)
    if yv > dv and yv <= 21:
        print("You win.")
    elif dv > yv and dv <= 21:
        print("Dealer wins.")
    else:
        print("Push.")


def status(yours, dealers):
    print("==============================")
    show_your_cards(yours)
    show_dealer_cards(dealers)
    print("==============================")


play = input("Do you want to play a game of Blackjack? (y/n): ")
while play == 'y':
    os.system('clear')
    deck = new_deck()
    your_cards = []
    dealer_cards = []
    for x in range(0, 2):
        card = get_card(deck)
        your_cards.append(card)
        deck = remove_from_deck(deck, card)

    dc = card = get_card(deck)
    dealer_cards.append(dc)
    deck = remove_from_deck(deck, dc)

    show_your_cards(your_cards)
    show_dealer_cards(dealer_cards)

    while(input("Type 'h' to hit or 's' to stay: ") == 'h'):
        card = get_card(deck)
        your_cards.append(card)
        deck = remove_from_deck(deck, card)

        show_your_cards(your_cards)

        if (calculate_hand_value(your_cards) > 21):
            print("You busted.")
            exit(1)

    while(calculate_hand_value(dealer_cards) <= 16):
        card = get_card(deck)
        dealer_cards.append(card)
        deck = remove_from_deck(deck, card)

        status(your_cards, dealer_cards)

        if calculate_hand_value(dealer_cards) > 21:
            print("Dealer busted.")

    compare_hand(your_cards, dealer_cards)

    play = input("Play again?: ")

print("Goodbye")
