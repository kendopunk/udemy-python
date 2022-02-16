# Rock, Paper, Scissors
import random

acceptable_inputs = ['0', '1', '2', 'quit']
input_map = ['Rock', 'Paper', 'Scissors']

value = ''
quit = False
while not quit:
    value = input(
        "What do you choose?  0 for rock, 1 for paper and 2 for scissors: ")

    if not value in acceptable_inputs:
        print('Invalid value.')
        value = input(
            "What do you choose?  0 for rock, 1 for paper and 2 for scissors: ")

    if value == 'quit':
        print("Game over.")
        exit(1)

    print("You chose %s" % input_map[int(value)])

    computer_pick = random.choice(acceptable_inputs[:-1])

    print("The computer chose %s" % input_map[int(computer_pick)])

    if (value == computer_pick):
        print("DRAW")
    elif (value == '0' and computer_pick == '2') or (value == '1' and computer_pick == '0') or (value == '2' and computer_pick == '1'):
        print("You WIN")
    else:
        print("You LOSE")
