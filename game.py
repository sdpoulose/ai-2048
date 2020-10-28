from game_functions import *

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
