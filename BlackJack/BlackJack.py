# Building a black jack card game...
import random

# 52 cards deck
deck = [
    ['2h', '3h', '4h', '5h', '6h', '7h', '8h', '9h', 'Th', 'Jh', 'Qh', 'Kh', 'Ah'], 
    ['2s', '3s', '4s', '5s', '6s', '7s', '8s', '9s', 'Ts', 'Js', 'Qs', 'Ks', 'As'], 
    ['2c', '3c', '4c', '5c', '6c', '7c', '8c', '9c', 'Tc', 'Jc', 'Qc', 'Kc', 'Ac'], 
    ['2d', '3d', '4d', '5d', '6d', '7d', '8d', '9d', 'Td', 'Jd', 'Qd', 'Kd', 'Ad']]

# Dictionary for card values
values = {'2':2, '3':3, '4':4, '5':5, '6':6, '7':7, '8':8, '9':9, 'T':10, 'J':10, 'Q':10, 'K':10, 'A':11}

# Draws cards for player
cards = random.sample([card for suit in deck for card in suit], 2)

# Sum of values and output cleaning
total_value = sum(values[card[0]] for card in cards)
output = " ".join(cards)

print(f"Cards: {output}")
print(f"Total value: {total_value}")
