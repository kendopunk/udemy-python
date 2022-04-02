cards = ['A', 'A', 'B', 'C', 'D']
for index in range(cards.count('A')):
    print(index)
    print(cards[index])
    cards.remove('A')
    cards.append('Z')

print(cards)
