##############################
# day11/improved.py
# An improved version of Blackjack
##############################
import os
import random

card_values = {
    "1": 1, "2": 2, "3": 3, "4": 4, "5": 5,
    "6": 6, "7": 7, "8": 8, "9": 9, "10": 10,
    "J": 10, "Q": 10, "K": 10, "A": 11, "A1": 1
}


def new_deck():
    return [
        '2', '2', '2', '2', '3', '3', '3', '3', '4', '4', '4', '4', '5', '5', '5', '5',
        '6', '6', '6', '6', '7', '7', '7', '7', '8', '8', '8', '8', '9', '9', '9', '9',
        '10', '10', '10', '10', 'J', 'J', 'J', 'J', 'Q', 'Q', 'Q', 'Q',
        'K', 'K', 'K', 'K', 'A', 'A', 'A', 'A']


def deal_cards(deck, num_cards):
    cards = []
    for _ in range(0, num_cards):
        c = random.choice(deck)
        cards.append(c)
        deck.remove(c)

    return deck, cards


def is_blackjack(cards):
    return len(cards) == 2 and cards.count('A') == 1 and (
        cards.count('10') == 1 or cards.count(
            'J') == 1 or cards.count('Q') == 1 or cards.count('K') == 1
    )


def sum_cards(cards):
    sum = 0
    for card in cards:
        sum += card_values[card]

    return sum


def handle_aces(cards):
    if cards.count('A') > 0:
        sum = sum_cards(cards)
        while sum > 21:
            cards.remove('A')
            cards.append('A1')
            sum = sum_cards(cards)
        return cards

    return cards


def hand_value(cards):
    if is_blackjack(cards):
        return 0
    else:
        cards = handle_aces(cards)
        return sum_cards(cards)


def show_cards(prefix, cards, first_only):
    if first_only:
        print(f"{prefix}: ['{cards[0]}']")
    else:
        print(f"{prefix}: {cards} = {hand_value(cards)}")


def game_status(yours, dealers, first_only):
    print("==============================")
    show_cards("You:", yours, False)
    show_cards("Dealer:", dealers, first_only)
    print("==============================")


def compare_hands(p, d):
    pv = hand_value(p)
    dv = hand_value(d)

    if is_blackjack(p):
        if is_blackjack(d):
            print("PUSH.")
        else:
            print("YOU WIN!")
    elif is_blackjack(d):
        print("DEALER WINS.")
    elif pv > dv:
        if pv > 21:
            print("DEALER WINS.")
        else:
            print("YOU WIN!")
    elif dv > pv:
        if dv > 21:
            print("YOU WIN!")
        else:
            print("DEALER WINS.")
    else:
        print("PUSH.")


play = input("Do you want to play a game of Blackjack? (y/n): ")
while play == 'y':
    os.system('clear')
    game_on = True
    player_busted = False
    deck = new_deck()

    deck, player_cards = deal_cards(deck, 2)
    # player_cards = ['A', 'A', '9', '7']
    deck, dealer_cards = deal_cards(deck, 2)

    game_status(player_cards, dealer_cards, True)

    if is_blackjack(player_cards):
        game_on = False
        print("Blackjack!!!")

    # hit or stand
    while(game_on and not player_busted and input("\nType 'h' to hit or 's' to stay: ") == 'h'):
        deck, card = deal_cards(deck, 1)
        player_cards.extend(card)
        show_cards("- You hit", player_cards, False)
        if (hand_value(player_cards) > 21):
            print("")
            print("- You busted.")
            player_busted = True

    # dealer's turn
    if is_blackjack(dealer_cards):
        game_on = False
    while(game_on and not player_busted and hand_value(dealer_cards) <= 16):
        deck, card = deal_cards(deck, 1)
        dealer_cards.extend(card)
        print("")
        show_cards("- Dealer hits", dealer_cards, False)
        if (hand_value(dealer_cards) > 21):
            print("")
            print("- Dealer busted.")

    print("")
    game_status(player_cards, dealer_cards, False)
    print("")
    compare_hands(player_cards, dealer_cards)
    print("")
    play = input("Play again (y/n): ")

print("Thanks for playing.  Goodbye.")
