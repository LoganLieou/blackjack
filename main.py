import random
from typing import List
from utility import generate_filename, serialize, sum_hand

# TODO add betting
# TODO more rounds

def print_hand(hand: List[dict]) -> None:
    for card in hand:
        print(f"{card['rank']} of {card['suit']}")

# create the deck
suits = ['hearts', 'spades', 'clubs', 'diamonds']
ranks = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'J', 'Q', 'K', 'A']
deck = [{'suit': suit, 'rank': rank} for suit in suits for rank in ranks]

# shuffle the deck randomly each time
random.shuffle(deck)

# each person starts with two cards
player_hand = [deck.pop(), deck.pop()]
dealer_hand = [deck.pop(), deck.pop()]

# output the hand you have and dealer face up card
print("PLAYER HAND:")
print_hand(player_hand)
print("DEALER HAND:")
print(f"{dealer_hand[0]['rank']} of {dealer_hand[0]['suit']}")

yn = input("do you want to export the current position?\n")
if yn.upper() == "YES" or yn.upper() == "Y" or yn.upper() == "1":
    with open(f"{generate_filename(10)}.blackjack", "w+") as f:
        f.write(serialize(dealer_hand, player_hand))
        f.close()

# player turn
while True:
    choice = input("HIT/STAND\n")
    if choice.upper() == "HIT":
        player_hand.append(deck.pop())
        for card in player_hand:
            print(f"player has {card['rank']} of {card['suit']}")
        if (sum_hand(player_hand) > 21):
            print("BUST!")
            exit() # even if dealer bust you still lose
    elif choice.upper() == "STAND":
        break
    else:
        print("invalid input enter either hit or stand")
        exit()

# dealer stands on soft 17
while sum_hand(dealer_hand) < 17:
    dealer_hand.append(deck.pop())

print("DEALER HAND:")
print_hand(dealer_hand)

# find out who wins
# cases: dealer bust, 21 for both, push, dealer wins, you win 
dealer_value = sum_hand(dealer_hand)
player_value = sum_hand(player_hand)
if (dealer_value > 21):
    print("Dealer busts, you win!")
elif (dealer_value == 21 and player_value == 21):
    print("Blackjack you lose!")
elif (dealer_value == player_value):
    print("Push no money made...")
elif (player_value > dealer_value):
    print("You win!")
else:
    print("You lose!")