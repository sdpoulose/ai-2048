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
