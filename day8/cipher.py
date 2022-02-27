# vars
import string

game_on = True
allowed = list(string.ascii_lowercase)
max_allowed_index = len(allowed) - 1
quit_string = '*q'
msg = ''
offset = 0


def validate_message(word):
    ret = True
    for char in list(word):
        if char not in allowed:
            ret = False

    return ret


def encode_message(word, offset):

    lst = []
    for x in list(word):
        index = allowed.index(x)
        new_index = index + offset
        if new_index > max_allowed_index:
            new_index = new_index - max_allowed_index - 1

        lst.append(allowed[new_index])

    return ''.join(lst)


def decode_message(word, offset):

    lst = []
    for x in list(word):
        index = allowed.index(x)
        new_index = index - offset
        if new_index < 0:
            new_index = max_allowed_index + new_index + 1

        lst.append(allowed[new_index])

    return ''.join(lst)


while game_on:
    action = input(
        "$> type 'encode' to encrypt, 'decode' to decrypt, or '*q' to quit: ")

    if action == quit_string:

        game_on = False
    elif action == 'decode':
        print("The decoded message is: %s." % decode_message(msg, offset))
    elif action == 'encode':
        msg = input("$> Type your messsage: ").lower()
        if not validate_message(msg):
            print("Invalid sequence of characters")
        else:
            offset = int(input("$> enter offset: "))
            if offset > max_allowed_index:
                offset = offset % max_allowed_index

            msg = encode_message(msg, offset)
            print("Here's the encoded result: %s." % msg)
    else:
        print("Invalid input.")
        exit(1)

print("Goodbye")

# Type 'encode' to encrypt or 'decode' to decrypt
# encode
# Type your message
# input()
# Type the shift number
# input()
# Here's the encoded result: lasfjsalfkajfa

# Type 'yes' if you want to go again.  Otherwise type 'no'
