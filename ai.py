from game_functions import *


max_tiles_up = []
max_tiles_down = []
max_tiles_left = []
max_tiles_right = []


def ai_next_move(game_state):

    orig_game_state = game_state

    for i in range(10):
        move_up(game_state)
        max_tiles_up.append(get_max_tile(game_state))
        get_blanks(game_state)
        ai_next_move(game_state)

    for i in range(10):
        move_down(game_state)
        max_tiles_down.append(get_max_tile(game_state))
        get_blanks(game_state)
        ai_next_move(game_state)

    for i in range(10):
        move_left(game_state)
        max_tiles_left.append(get_max_tile(game_state))
        get_blanks(game_state)
        ai_next_move(game_state)

    for i in range(10):
        move_right(game_state)
        max_tiles_right.append(get_max_tile(game_state))
        get_blanks(game_state)
        ai_next_move(game_state)

    up_score = sum(max_tiles_up)/len(max_tiles_up)
    down_score = sum(max_tiles_down)/len(max_tiles_down)
    left_score = sum(max_tiles_left)/len(max_tiles_left)
    right_score = sum(max_tiles_right)/len(max_tiles_right)

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

        max_tiles_up = []
        max_tiles_down = []
        max_tiles_left = []
        max_tiles_right = []

        ai_next_move(game_state)

##


ai_move(game_state, game_on)
