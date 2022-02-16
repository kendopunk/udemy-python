# Choose Your Own Adventure
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")
print("Your at a crossroads.  Where do you want to go?  Type \"left\" or \"right\".")

direction = 'none'
while direction != 'left' and direction != 'right':
    direction = input("$> direction: ").lower()

if direction == 'right':
    print("Game over.")
    exit(1)

print("You come to a lake.  There is an island in the middle of the lake.  Type \"wait\" to wait for a boat.  Type \"swim\" to swim across.")

swim_wait = 'none'
while swim_wait != 'swim' and swim_wait != 'wait':
    swim_wait = input("$> swim or wait: ").lower()

if swim_wait == 'swim':
    print("Game over.")
    exit(1)

print("You arrive at the island unharmed.  There is a house with 3 doors.  One red, one yellow and one blue.  Which color do you choose?")

color = 'none'
while color != 'red' and color != 'yellow' and color != 'blue':
    color = input("$> color: ").lower()

if color == 'red' or color == 'blue':
    print("Game over.")
    exit(1)

print("You win.")
