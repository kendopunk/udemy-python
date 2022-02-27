####################
# vars
####################
from random import choice


word_list = ['strawberry', 'friendship', 'everything', 'appreciate', 'motivation',
             'dizzying', 'bedazzling', 'puzzlement', 'razzmatazz', 'jazzercise', 'squeezebox']
word = choice(word_list)
num_tries = 6
try_count = 0
tally = ['_' for _ in list(word)]
matches = []


def print_tally(tally):
    print(tally)


def adjust_tally(tally, letter):
    indices = [i for i, x in enumerate(list(word)) if x == letter]
    for index in indices:
        tally[index] = letter

    return tally


def word_complete(tally):
    indices = [i for i, x in enumerate(tally) if x == '_']
    if len(indices) > 0:
        return False
    return True


print(tally)

while try_count < num_tries:

    letter = input("$> enter letter: ").lower()
    if letter == 'quit':
        print('Goodbye')
        exit(1)
    elif letter in matches:
        print("You already guessed %s" % letter)
    else:
        matches.append(letter)
        if letter in word:
            tally = adjust_tally(tally, letter)
            print("You have a match")
            if (word_complete(tally)):
                print("You win.  Game over.\n")
                exit(1)
        else:
            print("Strike !!\n")
            try_count += 1
            print("%d tries left.\n\n" % (num_tries - try_count))

    print(tally)

print("Game over.  The word was %s." % word)
