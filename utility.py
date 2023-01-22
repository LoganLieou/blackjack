# card object: {'suit': suit, 'rank': rank}
# if there's an ace soft total else hard total
# output this to a file
import random
import string
from typing import List

def sum_hand(hand: List[dict]) -> int:
    r = 0
    for card in hand:
        rank = card['rank']
        if (rank == 'J' or rank == 'Q' or rank == 'K'):
            r += 10
        elif (rank == 'A'):
            r += 1 if r + 10 > 21 else 11
        else:
            r += int(rank)
    return r

def generate_filename(length):
    return ''.join(random.choices(string.ascii_letters, k=length))

def serialize(dealer: List[dict], player: List[dict]) -> str:
    state = 'HARD'
    # player soft sum
    if ('A' in [card['rank'] for card in player]):
        state = 'SOFT'
    return f"{state},UC:{sum_hand([dealer[0]])},PT:{sum_hand(player)}"
