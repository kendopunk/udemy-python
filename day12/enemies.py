enemies = 10


def increase_enemies():
    print(f"enemies inside function = {enemies}")
    print(enemies)
    return enemies + 1


enemies = increase_enemies()
print(f"enemies outside function = {enemies}")
