print("Welcome to the tip calculator")
total = input("What was the total bill? $")
num_people = input("How many people to split the bill? ")
pct = input("What percentage tip would you like to give? 0, 10, 12 or 15: ")

try:
    total = float(total)
except ValueError as inst:
    print("Invalid value for total bill.")
    print(type(inst))
    exit(1)

try:
    num_people = int(num_people)
except ValueError as inst:
    print("Invalid value for number of people.")
    print(type(inst))
    exit(1)

try:
    pct = int(pct)
    if pct not in [0, 10, 12, 15]:
        raise Exception
except ValueError as inst:
    print("Invalid value for percentage.")
    print(type(inst))
    exit(1)
except Exception as inst:
    print("Please choose percentage from specified options.")
    print(type(inst))
    exit(1)


print("Each person should pay $%s." %
      '{:.2f}'.format(((total + (total * pct/100))/num_people)))
