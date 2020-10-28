from player import *
import random
from initial_state import *


def get_blanks(game_state):
    blank_tiles = []
    for tile in game_state:
        if tile.value == 0:
            blank_tiles.append(tile.id)
    # print(len(blank_tiles))
    new_tile = random.randint(1, len(blank_tiles)) - 1
    new_tile_id = blank_tiles[new_tile - 1]
    # print(new_tile_id)
    if random.randint(1, 5) == 1:
        game_state[new_tile_id].value = 4
    else:
        game_state[new_tile_id].value = 2


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


while(1):
    if game_on == False:
        break
    refresh_game(game_state, game_on)
    print("Press 'q' + 'Enter' to exit.")
    print("Use AWSD + 'Enter' to play")
    next_move = input()
    if next_move == 'q':
        game_on = False
    elif next_move == 'w':
        move_up(game_state)
    elif next_move == 's':
        move_down(game_state)
    elif next_move == 'a':
        move_left(game_state)
    elif next_move == 'd':
        move_right(game_state)
    get_blanks(game_state)
