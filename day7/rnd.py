from random import choice

word_list = ['aardvark', 'baboon', 'camel']

chosen_word = choice(word_list)

guess = input("$> enter a guess: ").lower()
if guess in chosen_word:
    print("%s is in %s" % (guess, chosen_word))
else:
    print("%s does not exist in %s" % (guess, chosen_word))
