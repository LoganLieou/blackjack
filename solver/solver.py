# since blackjack is a solved game this should just be a hash map
# we can solve any position in blackjack in O(1) time

# let's read in the state of a blackjack game we can encode this using a special
# serialization algorithm

# this is three tuple that stores the value of the two hand sums
# and weather or not the sums are hard / soft
from dataclasses import dataclass

@dataclass
class Game:
    state: str
    dealer: int
    player: int

filename = input("Blackjack file to be read:\n")

# read in blackjack file contents
with open(filename, 'r') as f:
    game = f.read()
    f.close()

# TODO implment the deserializer
def deserialize(game: str) -> Game:
    nodes = game.split(',')
    return Game(nodes[0], int(nodes[1][3:]), int(nodes[2][3:]))

# game object gives us up card hand sum
# and soft / hard sum
observation_space = deserialize(game)

# solve the game of blackjack
action_space = ['hit', 'stand', 'double down']

hard_solution = [['hit'] * 22] * 22
soft_solution = [['hit'] * 22] * 22

# output the solution to the problem
if (observation_space.state == 'HARD'):
    print(hard_solution[observation_space.player][observation_space.dealer])
elif (observation_space.state == 'SOFT'):
    print(soft_solution[observation_space.player][observation_space.dealer])
