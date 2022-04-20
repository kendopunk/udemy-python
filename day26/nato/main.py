# day26/nato/main.py
# create a dictionary from the CSV
# convert any name to NATO
import re
import pandas as p

df = p.read_csv('./nato_phonetic_alphabet.csv')
nato_dict = {}
for (_, row) in df.iterrows():
    nato_dict[row.letter] = row.code

running = True
while running:
    name = re.sub('\s+', '', input("Enter a proper name or 'q' to quit: "))
    if name == 'q':
        running = False
        print("Game over.")
    else:
        nato_representation = [nato_dict[n] for n in name.upper()]
        print(f"{name} is {'-'.join(nato_representation)}")
