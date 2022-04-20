import random


new_dict = {k: str(k) + 'fred' for k in range(1, 5)}
print(new_dict)

second_dict = {key: value.upper()
               for (key, value) in new_dict.items() if key > 2}
print(second_dict)

print(second_dict.items())

students = ['Fred', 'Marge', 'Chad', 'Wopper', 'Bilbo']
scores = {k: random.randint(1, 100) for k in students}
print(scores)

# scores -> new dictionary
passed_students = {k: v for (k, v) in scores.items() if v >= 70}
print(passed_students)
