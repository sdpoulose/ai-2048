from game_functions import *
import time
import copy
import random

up_max = []
down_max = []
left_max = []
right_max = []


def simulate_first_move_up(game_state):
    game_state_up = copy.deepcopy(game_state)
    get_blanks(game_state_up)
    move_up(game_state)
    for iter in range(10):
        next_move = random.randint(1, 4)
        if next_move == 1:
            move_up(game_state_up)
        elif next_move == 2:
            move_down(game_state_up)
        elif next_move == 3:
            move_left(game_state_up)
        else:
            move_right(game_state_up)
    up_max.append(get_empty_tile(game_state_up))


def simulate_first_move_down(game_state):
    game_state_down = copy.deepcopy(game_state)
    get_blanks(game_state_down)
    move_down(game_state)
    for iter in range(10):
        next_move = random.randint(1, 4)
        if next_move == 1:
            move_up(game_state_down)
        elif next_move == 2:
            move_down(game_state_down)
        elif next_move == 3:
            move_left(game_state_down)
        else:
            move_right(game_state_down)
    down_max.append(get_empty_tile(game_state_down))


def simulate_first_move_left(game_state):
    game_state_left = copy.deepcopy(game_state)
    get_blanks(game_state_left)
    move_left(game_state)
    for iter in range(10):
        next_move = random.randint(1, 4)
        if next_move == 1:
            move_up(game_state_left)
        elif next_move == 2:
            move_down(game_state_left)
        elif next_move == 3:
            move_left(game_state_left)
        else:
            move_right(game_state_left)
    left_max.append(get_empty_tile(game_state_left))


def simulate_first_move_right(game_state):
    game_state_right = copy.deepcopy(game_state)
    get_blanks(game_state_right)
    move_right(game_state)
    for iter in range(10):
        next_move = random.randint(1, 4)
        if next_move == 1:
            move_up(game_state_right)
        elif next_move == 2:
            move_down(game_state_right)
        elif next_move == 3:
            move_left(game_state_right)
        else:
            move_right(game_state_right)
    right_max.append(get_empty_tile(game_state_right))


def choose_best_move(up_max, down_max, left_max, right_max):
    empty_tile_list = []
    empty_tile_list.append(sum(up_max))
    empty_tile_list.append(sum(down_max))
    empty_tile_list.append(sum(left_max))
    empty_tile_list.append(sum(right_max))
    if max(empty_tile_list) == sum(up_max):
        move_up(game_state)
    elif max(empty_tile_list) == sum(down_max):
        move_down(game_state)
    elif max(empty_tile_list) == sum(left_max):
        move_left(game_state)
    else:
        move_right(game_state)
    get_blanks(game_state)
    refresh_game(game_state, game_on)
    up_max = []
    down_max = []
    left_max = []
    right_max = []
