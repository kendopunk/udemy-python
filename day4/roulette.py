import random
import re

total_bill = 127.33

names = re.split(
    r",\s+", input('Give me everyone\'s name, separated by a comma: '))

random_index = random.randrange(0, len(names))
print("%s has to pay the total bill of $%s" %
      (names[random_index], format(total_bill, '.2f')))

print("Using choice()...")
print("%s has to pay the total bill of $%s" %
      (random.choice(names), format(total_bill, '.2f')))
