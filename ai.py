from game_functions import *
import time

level = 1

max_tiles_up = []
max_tiles_down = []
max_tiles_left = []
max_tiles_right = []


def ai_sequent_move(game_state, max_list, level):

    game_state_copy_1 = game_state
    game_state_copy_2 = game_state
    game_state_copy_3 = game_state
    game_state_copy_4 = game_state

    level += 1

    move_up(game_state_copy_1)

    if level < 5:
        max_list.append(get_max_tile(game_state_copy_1))
        get_blanks(game_state_copy_1)
        ai_sequent_move(game_state_copy_1, max_list, level)

    move_down(game_state_copy_2)

    if level < 5:
        max_list.append(get_max_tile(game_state_copy_2))
        get_blanks(game_state_copy_2)
        ai_sequent_move(game_state_copy_2, max_list, level)

    move_left(game_state_copy_3)

    if level < 5:
        max_list.append(get_max_tile(game_state_copy_3))
        get_blanks(game_state_copy_3)
        ai_sequent_move(game_state_copy_3, max_list, level)

    move_right(game_state_copy_4)

    if level < 5:
        max_list.append(get_max_tile(game_state_copy_4))
        get_blanks(game_state_copy_4)
        ai_sequent_move(game_state_copy_4, max_list, level)


def ai_next_move_up(game_state):
    move_up(game_state)

    game_state_up = game_state

    ai_sequent_move(game_state_up, max_tiles_up, level)


def ai_next_move_down(game_state):
    move_down(game_state)

    game_state_down = game_state

    ai_sequent_move(game_state_down, max_tiles_down, level)


def ai_next_move_left(game_state):
    move_left(game_state)

    game_state_left = game_state

    ai_sequent_move(game_state_left, max_tiles_left, level)


def ai_next_move_right(game_state):
    move_right(game_state)

    game_state_right = game_state

    ai_sequent_move(game_state_right, max_tiles_right, level)


def ai_next_move(game_state):

    max_tiles_up = []
    max_tiles_down = []
    max_tiles_left = []
    max_tiles_right = []

    orig_game_state = game_state

    game_state_up = game_state
    game_state_down = game_state
    game_state_left = game_state
    game_state_right = game_state

    ai_next_move_up(game_state_up)
    ai_next_move_down(game_state_down)
    ai_next_move_left(game_state_left)
    ai_next_move_right(game_state_right)

    if len(max_tiles_up) != 0:
        up_score = sum(max_tiles_up)/len(max_tiles_up)
    elif len(max_tiles_down) != 0:
        down_score = sum(max_tiles_down)/len(max_tiles_down)
    elif len(max_tiles_left) != 0:
        left_score = sum(max_tiles_left)/len(max_tiles_left)
    elif len(max_tiles_right) != 0:
        right_score = sum(max_tiles_right)/len(max_tiles_right)
    else:
        up_score, down_score, left_score, right_score = 0, 0, 0, 0

    true_max = max(up_score, down_score, left_score, right_score)

    if true_max == up_score:
        move_up(orig_game_state)

    elif true_max == down_score:
        move_down(orig_game_state)

    elif true_max == left_score:
        move_left(orig_game_state)

    elif true_max == right_score:
        move_right(orig_game_state)

    refresh_game(orig_game_state, game_on)


def ai_move(game_state, game_on):

    for i in range(10):
        # time.sleep(0.5)
        ai_next_move(game_state)


##
ai_move(game_state, game_on)
