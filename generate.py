import random
#from random import choice

#coin = random.choice(["heads","tails"])
#coin = choice(["heads","tails"])
#print(coin)

#number = random.randint(1, 10)
cards = ["Tri","Ly","Viet"]
#print(number)
# Trộn vị trí
random.shuffle(cards)
for card in cards:
    print(card)