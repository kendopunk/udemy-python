import random

min = 0
max = 1
count = 0
while count < 10:
    num = random.randrange(min, max + 1)
    if num == 0:
        print("%d - Heads" % num)
    elif num == 1:
        print("%d - Tails" % num)
    else:
        print("%d - OOB" % num)
    count += 1
