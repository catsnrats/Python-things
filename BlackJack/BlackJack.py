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
def deal_cards():
    return random.sample([card for suit in deck for card in suit], 2)

player_cards = deal_cards()
dealer_cards = deal_cards()

# Calculates hands total value
def calculate_total(cards):
    return sum(values[card[0]] for card in cards)

player_value = calculate_total(player_cards)
dealer_value = calculate_total(dealer_cards)
player = " ".join(player_cards)

print(f"Players cards: {player}")
print(f"Total value: {player_value}")

print(f"(Dealers visible card: {dealer_cards[0]})\n")

# Loop to handle players choice...
while True:
    choice = input("Hit or Stay? ").lower()
    if choice == 'hit':
        # Draws a new card
        #new_card = deal_cards()
        new_card = random.choice([card for suit in deck for card in suit])
        player_cards.append(new_card)
        player_value += values[new_card[0]]
        # Some output
        print("New card: ", new_card)
        print("Updated hand", ' '.join(player_cards))
        print("Updated total value", player_value)

        if player_value > 21:
            print("\nPlayer went over 21!")
            break

    elif choice == 'stay':
        break

    else:
        print("Invalid choice. Write 'hit' or 'stay'.")

# Dealer's turn ### (CHECK THIS AGAIN) ###
while dealer_value <= 16:
    new_card = random.choice([card for suit in deck for card in suit])
    #new_card = deal_cards()
    dealer_cards.append(new_card)
    dealer_value = calculate_total(dealer_cards)
    
    print("\nDealer Draws:", new_card)

# Find the winner...
if dealer_value > 21:
    print("Dealer went over 21!")
    exit()
if player_value == dealer_value:
    print("\nEVEN")
elif player_value <= 21 and player_value > dealer_value:
    print("\nPLAYER WINS")
elif dealer_value <= 21 and dealer_value > player_value:
    print("\nDEALER WINS")

print("\nDealers hand:", ' '.join(dealer_cards))
print(f"Dealers value: {dealer_value} \n")

print("Players final hand:", ' '.join(player_cards))
print(f"Players value: {player_value}")

