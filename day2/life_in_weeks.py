print("Your Life in Weeks")
print("=" * 75)

age = input("What is your current age? ")

try:
    age = float(age)
except ValueError:
    print("Invalid age.")
    exit(1)

try:
    if int(age) >= 90:
        raise Exception
except Exception:
    print("Age too high.")
    exit(1)

print(round(age))

max_age = 90
days = (max_age - age) * 365
weeks = (max_age - age) * 52
months = (max_age - age) * 12

print(
    f"You have {round(days)} days, {round(weeks)} weeks, and {round(months)} months left.")
