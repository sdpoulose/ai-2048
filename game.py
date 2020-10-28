from tile import *

game_state = [tile_1, tile_2, tile_3, tile_4,
              tile_5, tile_6, tile_7, tile_8,
              tile_9, tile_10, tile_11, tile_12,
              tile_13, tile_14, tile_15, tile_16]


def refresh_game():
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


def move_up():
    pass


def move_down():
    pass


def move_left():
    pass


def move_right():
    pass


while(1):
    refresh_game()
    print("Press 'q' + 'Enter' to exit.")
    next_move = input()
    if next_move == 'q':
        break
