import py_compile
from re import I


def checkIsPrime(num):
    isPrime = True
    if num <= 1:
        isPrime = False
    else:
        for i in range(2, num):
            if num % i == 0:
                isPrime = False
                break

    return isPrime


# number = input("$> enter number to check: ")
# try:
#     i = int(number)
#     print("Is %d prime?   %r." % (i, checkIsPrime(i)))
# except ValueError:
#     print("Invalid number.")
#     exit(1)

for x in range(1500, 1600):
    if checkIsPrime(x):
        print("%d is a prime." % x)
