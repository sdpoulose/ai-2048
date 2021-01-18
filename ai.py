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
# to simulate all possible movesets for the game


def ai_first_move_up(game_state):
    game_state_first_up = copy.deepcopy(game_state)
    move_up(game_state_first_up)
    get_blanks(game_state_first_up)

    ai_sequent_moves(game_state_first_up, up_max)


def ai_first_move_down(game_state):
    game_state_first_down = copy.deepcopy(game_state)
    move_up(game_state_first_down)
    get_blanks(game_state_first_down)

    ai_sequent_moves(game_state_first_down, down_max)


def ai_first_move_right(game_state):
    game_state_first_right = copy.deepcopy(game_state)
    move_up(game_state_first_right)
    get_blanks(game_state_first_right)

    ai_sequent_moves(game_state_first_right, right_max)


def ai_first_move_left(game_state):
    game_state_first_left = copy.deepcopy(game_state)
    move_up(game_state_first_left)
    get_blanks(game_state_first_left)

    ai_sequent_moves(game_state_first_left, left_max)


# recursive function for all possible moves
def ai_sequent_moves(game_state, max_list):

    global level
    level += 1


# calculate most favorable first move and apply it
'''
def choose_best_move():
    true_max_list = []

    global up_max
    global down_max
    global left_max
    global right_max

    true_max_list.append(max(up_max))
    true_max_list.append(max(down_max))
    true_max_list.append(max(left_max))
    true_max_list.append(max(right_max))

    true_max = max(true_max_list)

    if(true_max == max(up_max)):
        move_up(game_state)
    elif(true_max == max(down_max)):
        move_down(game_state)
    elif(true_max == max(left_max)):
        move_left(game_state)
    elif(true_max == max(right_max)):
        move_right(game_state)

    refresh_game(game_state, game_on)


# simulate the ai by repeatedly looking 5 steps ahead and
# choosing the best move to reach a win condition
def simulate_game_traversal(game_state):
    for i in range(10):
        ai_first_move_up(game_state)
        ai_first_move_down(game_state)
        ai_first_move_left(game_state)
        ai_first_move_right(game_state)
        choose_best_move()
        # up_max = []
        # down_max = []
        # left_max = []
        # right_max = []


simulate_game_traversal((game_state))

'''
