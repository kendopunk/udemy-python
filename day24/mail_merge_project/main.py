# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

marker = "[name]"

template = open("./Input/Letters/starting_letter.txt", "r")
template_content = template.read()

with open("./Input/Names/invited_names.txt", "r") as invite_list:
    invitees = invite_list.readlines()

for name in invitees:
    letter_contents = template_content.replace(marker, name.strip())
    with open("./Output/letter_to_" + name.strip() + '.txt', mode="w") as letter:
        letter.write(letter_contents)
        letter.close()

template.close()
invite_list.close()

print("Mail merge successfully executed.")
