from functools import reduce


print("Data type excercise")
num = input("Enter any 3 digit number: ")

if (len(num) != 3):
    raise Exception("Must be a two-digit number.")
    exit(1)

try:
    to_int = int(num)
except ValueError as inst:
    print("Invalid value for 3-digit number")
    print(type(inst))
    exit(1)

parts = list(num)
print("%s + %s + %s = %d" %
      (parts[0], parts[1], parts[2], reduce(lambda a, b: int(a) + int(b), parts)))
