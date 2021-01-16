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

# first move defined, then branch out with all possible moves
# make a copy of game state so as to not effect the original
# then make a clearly defined first move on the game state copy
# and finally create all possible branches


def ai_first_move_up(game_state):
    game_state_first_up = copy.deepcopy(game_state)
    move_up(game_state_first_up)
    get_blanks(game_state_first_up)

    ai_sequent_moves(game_state_first_up)


def ai_first_move_down(game_state):
    game_state_first_down = copy.deepcopy(game_state)
    move_up(game_state_first_down)
    get_blanks(game_state_first_down)

    ai_sequent_moves(game_state_first_down)


def ai_first_move_right(game_state):
    game_state_first_right = copy.deepcopy(game_state)
    move_up(game_state_first_right)
    get_blanks(game_state_first_right)

    ai_sequent_moves(game_state_first_right)


def ai_first_move_left(game_state):
    game_state_first_left = copy.deepcopy(game_state)
    move_up(game_state_first_left)
    get_blanks(game_state_first_left)

    ai_sequent_moves(game_state_first_left)


# recursive function for all possible moves
def ai_sequent_moves(game_state):
    while(level < 5):
        game_state_up = copy.deepcopy(game_state)
        game_state_down = copy.deepcopy(game_state)
        game_state_left = copy.deepcopy(game_state)
        game_state_right = copy.deepcopy(game_state)


# calculate most favorable first move and apply it
def simulate_game_traversal(game_state):
    pass
