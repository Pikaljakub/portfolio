import random
deck = []
colors=("A","B","C","D")
values = ("1","2","3","4","5","6","7","8","9","10","J","Q","K")
for color in colors:
    for value in values:
        deck.append(color + value)
random.shuffle(deck)
print(deck)
print(deck.pop())
print(deck.pop())
print(deck)
print(len(deck), "karet")