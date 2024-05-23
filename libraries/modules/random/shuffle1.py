import random 

cards = ["jack", "queen", "king", "ace"]
random.shuffle(cards)
# we need to make a for loop in order for the list to be shuffled in this case
for card in cards:
    print(card)

# expected output:
# randomized version of the list of cards
# king
# jack
# queen
# ace