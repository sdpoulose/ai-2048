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
