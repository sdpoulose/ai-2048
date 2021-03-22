"""

from game_functions import *
import time
import copy

level_up = 1  # level of traversal tree
level_down = 1
level_left = 1
level_right = 1
test
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

    ai_sequent_moves_up(game_state_first_up, up_max)


def ai_first_move_down(game_state):
    game_state_first_down = copy.deepcopy(game_state)
    move_up(game_state_first_down)
    get_blanks(game_state_first_down)

    ai_sequent_moves_down(game_state_first_down, down_max)


def ai_first_move_left(game_state):
    game_state_first_left = copy.deepcopy(game_state)
    move_up(game_state_first_left)
    get_blanks(game_state_first_left)

    ai_sequent_moves_left(game_state_first_left, left_max)


def ai_first_move_right(game_state):
    game_state_first_right = copy.deepcopy(game_state)
    move_up(game_state_first_right)
    get_blanks(game_state_first_right)

    ai_sequent_moves_right(game_state_first_right, right_max)


# recursive function for all possible moves
def ai_sequent_moves_up(game_state, max_list):

    global level_up

    if level_up < 336:
        level_up += 1

        game_state_up = copy.deepcopy(game_state)
        game_state_down = copy.deepcopy(game_state)
        game_state_left = copy.deepcopy(game_state)
        game_state_right = copy.deepcopy(game_state)

        move_up(game_state_up)
        move_down(game_state_down)
        move_left(game_state_left)
        move_right(game_state_right)

        get_blanks(game_state_up)
        get_blanks(game_state_down)
        get_blanks(game_state_left)
        get_blanks(game_state_right)

        if(game_on):

            ai_sequent_moves_up(game_state_up, max_list)
            ai_sequent_moves_up(game_state_down, max_list)
            ai_sequent_moves_up(game_state_left, max_list)
            ai_sequent_moves_up(game_state_right, max_list)
    else:
        # max_list.append(get_sum_tile(game_state))
        max_list.append(get_max_tile(game_state))
        max_list.append(get_empty_tile(game_state))


def ai_sequent_moves_down(game_state, max_list):

    global level_down

    if level_down < 336:
        level_down += 1

        game_state_up = copy.deepcopy(game_state)
        game_state_down = copy.deepcopy(game_state)
        game_state_left = copy.deepcopy(game_state)
        game_state_right = copy.deepcopy(game_state)

        move_up(game_state_up)
        move_down(game_state_down)
        move_left(game_state_left)
        move_right(game_state_right)

        get_blanks(game_state_up)
        get_blanks(game_state_down)
        get_blanks(game_state_left)
        get_blanks(game_state_right)

        if(game_on):
            ai_sequent_moves_down(game_state_up, max_list)
            ai_sequent_moves_down(game_state_down, max_list)
            ai_sequent_moves_down(game_state_left, max_list)
            ai_sequent_moves_down(game_state_right, max_list)
    else:
        # max_list.append(get_sum_tile(game_state))
        max_list.append(get_max_tile(game_state))
        max_list.append(get_empty_tile(game_state))


def ai_sequent_moves_left(game_state, max_list):

    global level_left

    if level_left < 336:
        level_left += 1

        game_state_up = copy.deepcopy(game_state)
        game_state_down = copy.deepcopy(game_state)
        game_state_left = copy.deepcopy(game_state)
        game_state_right = copy.deepcopy(game_state)

        move_up(game_state_up)
        move_down(game_state_down)
        move_left(game_state_left)
        move_right(game_state_right)

        get_blanks(game_state_up)
        get_blanks(game_state_down)
        get_blanks(game_state_left)
        get_blanks(game_state_right)

        if(game_on):
            ai_sequent_moves_left(game_state_up, max_list)
            ai_sequent_moves_left(game_state_down, max_list)
            ai_sequent_moves_left(game_state_left, max_list)
            ai_sequent_moves_left(game_state_right, max_list)
    else:
        # max_list.append(get_sum_tile(game_state))
        max_list.append(get_max_tile(game_state))
        max_list.append(get_empty_tile(game_state))


def ai_sequent_moves_right(game_state, max_list):

    global level_right

    if level_right < 336:
        level_right += 1

        game_state_up = copy.deepcopy(game_state)
        game_state_down = copy.deepcopy(game_state)
        game_state_left = copy.deepcopy(game_state)
        game_state_right = copy.deepcopy(game_state)

        move_up(game_state_up)
        move_down(game_state_down)
        move_left(game_state_left)
        move_right(game_state_right)

        get_blanks(game_state_up)
        get_blanks(game_state_down)
        get_blanks(game_state_left)
        get_blanks(game_state_right)

        if(game_on):
            ai_sequent_moves_right(game_state_up, max_list)
            ai_sequent_moves_right(game_state_down, max_list)
            ai_sequent_moves_right(game_state_left, max_list)
            ai_sequent_moves_right(game_state_right, max_list)
    else:
        # max_list.append(get_sum_tile(game_state))
        max_list.append(get_max_tile(game_state))
        max_list.append(get_empty_tile(game_state))

# calculate most favorable first move and apply it


def choose_best_move(up_max, down_max, left_max, right_max):
    true_max_list = []

    true_max_list.append(sum(up_max)/len(up_max))
    true_max_list.append(sum(down_max)/len(down_max))
    true_max_list.append(sum(left_max)/len(left_max))
    true_max_list.append(sum(right_max)/len(right_max))

    true_max = max(true_max_list)

    '''
    print(up_max)
    print(down_max)
    print(left_max)
    print(right_max)
    '''

    if(true_max == true_max_list[0]):
        move_up(game_state)
    elif(true_max == true_max_list[1]):
        move_down(game_state)
    elif(true_max == true_max_list[2]):
        move_left(game_state)
    elif(true_max == true_max_list[3]):
        move_right(game_state)

    get_blanks(game_state)
    '''
    print("up")
    print(len(up_max))

    print("\ndown")
    print(len(down_max))

    print("\nleft")
    print(len(left_max))

    print("\nright")
    print(len(right_max))
    '''

    up_max = []
    down_max = []
    left_max = []
    right_max = []

    global level_up
    global level_down
    global level_left
    global level_right

    level_up = 0
    level_down = 0
    level_left = 0
    level_right = 0

    refresh_game(game_state, game_on)


# simulate the ai by repeatedly looking 5 steps ahead and
# choosing the best move to reach a win condition
def simulate_game_traversal(game_state):
    for i in range(100):
        ai_first_move_up(game_state)
        ai_first_move_down(game_state)
        ai_first_move_left(game_state)
        ai_first_move_right(game_state)
        choose_best_move(up_max, down_max, left_max, right_max)


simulate_game_traversal((game_state))

"""

print("las vegas ai needs some fixing,\nplease use <python3 ai_monte_carlo> instead")
