from tile import *
import random

game_state = [tile_1, tile_2, tile_3, tile_4,
              tile_5, tile_6, tile_7, tile_8,
              tile_9, tile_10, tile_11, tile_12,
              tile_13, tile_14, tile_15, tile_16]

game_on = True


def get_blanks(game_state):
    blank_tiles = []
    for tile in game_state:
        if tile.value == 0:
            blank_tiles.append(tile.id)
    new_tile_id = random.randint(1, len(blank_tiles))
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
                print("| " + str(tile.value) + "|", end='')
            else:
                print("| " + str(tile.value), end='')
        print("")
    print("", end='')
    print("_____________")


def move_up(game_state):
    pass


def move_down(game_state):
    pass


def move_left(game_state):
    pass


def move_right(game_state):
    pass


while(1):
    if game_on == False:
        break
    refresh_game(game_state, game_on)
    print("Press 'q' + 'Enter' to exit.")
    next_move = input()
    if next_move == 'q':
        game_on = False
    get_blanks(game_state)
