for x in range(1, 101):
    if x % 5 == 0 and x % 3 == 0:
        print("%d: %s" % (x, "FizzBuzz"))
    elif x % 3 == 0:
        print("%d: %s" % (x, "Fizz"))
    elif x % 5 == 0:
        print("%d: %s" % (x, "Buzz"))
    else:
        print(x)
