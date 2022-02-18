from random import choice, sample

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')']
letters = []
ucase = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L',
         'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
for letter in ucase:
    letters.append(letter)
    letters.append(letter.lower())

num_letters = int(input("How many letters would you like in your password? "))
num_symbols = int(input("How many symbols would you like in your password? "))
num_numbers = int(input("How many numbers would you like in your password? "))

password_as_list = []

# letters
for x in range(1, num_letters + 1):
    password_as_list.append(choice(letters))

# symbols
for x in range(1, num_symbols + 1):
    password_as_list.append(choice(symbols))

# numbers
for x in range(1, num_numbers + 1):
    password_as_list.append(choice(numbers))

shuffled = sample(password_as_list, len(password_as_list))

print("Your password is %s." % ''.join(shuffled))
