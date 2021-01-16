from game_functions import *
import time
import copy

level = 1  # level of traversal tree

#
# lists to contain maximum values of game state
# after 5 levels of traversal in the decision tree
# grouped by first move
#
up_max = []
down_max = []
left_max = []
right_max = []

for i in range(5):
    for tile in game_state:
        print(tile.value)
    get_blanks(game_state)


def simulate_game_traversal(game_state):
    pass
