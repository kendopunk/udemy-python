MIN = 0
MAX = 100
for number in range(MIN, MAX+1):
    if number % 3 == 0 and number % 5 == 0:
        print(f"{number}: FizzBuzz")
    elif number % 3 == 0:
        print(f"{number}: Fizz")
    elif number % 5 == 0:
        print(f"{number}: Buzz")
    else:
        print(number)
