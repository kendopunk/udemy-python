row1 = ["😋", "😋", "😋"]
row2 = ["😋", "😋", "😋"]
row3 = ["😋", "😋", "😋"]

map = [row1, row2, row3]
print(f"{row1}\n{row2}\n{row3}")

acceptable_inputs = []
for x in range(0, 3):
    for y in range(0, 3):
        acceptable_inputs.append(str(x) + str(y))

quit = False

while not quit:
    position = input("$> enter position or quit to stop: ")
    if position == 'quit':
        print("Game over.")
        quit = True
        exit(0)

    if not position in acceptable_inputs:
        print('Invalid value.')
    else:
        lst = list(position)
        row = int(lst[0])
        col = int(lst[1])

        map[row][col] = 'X'

        print(f"{row1}\n{row2}\n{row3}")
