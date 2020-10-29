from player import *
import random
from initial_state import *


def get_blanks(game_state):
    blank_tiles = []
    for tile in game_state:
        if tile.value == 0:
            blank_tiles.append(tile.id)
    # print(len(blank_tiles))

    if len(blank_tiles) > 0:
        new_tile = random.randint(0, len(blank_tiles) - 1)
        new_tile_id = blank_tiles[new_tile]
        # print(new_tile_id)
        if random.randint(1, 5) == 1:
            game_state[new_tile_id - 1].value = 4
        else:
            game_state[new_tile_id - 1].value = 2


def check_game_on(game_state):
    for tile in game_state:
        if tile.value == 2048:
            game_state = False


def refresh_game(game_state, game_on):
    print("_____________")
    for i in range(4):
        for tile in game_state[4*i:4*i+4]:
            if (tile.id % 4) == 0:
                print("| " + str(tile.value) + " |", end='')
            else:
                print("| " + str(tile.value), end='')
        print("")
    print("", end='')
    print("_____________")


def get_max_tile(game_state):
    max = 0
    for tile in game_state:
        if tile.id > max:
            max = tile.id
    return max
