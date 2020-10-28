
def move_up(game_state):
    for iter in range(3):
        for i in range(5, 9):
            if game_state[i - 5].value == 0:
                game_state[i - 5].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i - 5].value == game_state[i - 1].value:
                game_state[i - 5].value += game_state[i - 1].value
                game_state[i - 1].value = 0

        for i in range(9, 13):
            if game_state[i - 5].value == 0:
                game_state[i - 5].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i - 5].value == game_state[i - 1].value:
                game_state[i - 5].value += game_state[i - 1].value
                game_state[i - 1].value = 0

        for i in range(13, 17):
            if game_state[i - 5].value == 0:
                game_state[i - 5].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i - 5].value == game_state[i - 1].value:
                game_state[i - 5].value += game_state[i - 1].value
                game_state[i - 1].value = 0


def move_down(game_state):
    for iter in range(3):
        for i in range(9, 13):
            if game_state[i + 3].value == 0:
                game_state[i + 3].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i + 3].value == game_state[i - 1].value:
                game_state[i + 3].value += game_state[i - 1].value
                game_state[i - 1].value = 0
        for i in range(5, 9):
            if game_state[i + 3].value == 0:
                game_state[i + 3].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i + 3].value == game_state[i - 1].value:
                game_state[i + 3].value += game_state[i - 1].value
                game_state[i - 1].value = 0
        for i in range(1, 5):
            if game_state[i + 3].value == 0:
                game_state[i + 3].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i + 3].value == game_state[i - 1].value:
                game_state[i + 3].value += game_state[i - 1].value
                game_state[i - 1].value = 0


def move_left(game_state):
    for iter in range(3):
        for i in range(2, 15, 4):
            if game_state[i - 2].value == 0:
                game_state[i - 2].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i - 2].value == game_state[i - 1].value:
                game_state[i - 2].value += game_state[i - 1].value
                game_state[i - 1].value = 0
        for i in range(3, 16, 4):
            if game_state[i - 2].value == 0:
                game_state[i - 2].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i - 2].value == game_state[i - 1].value:
                game_state[i - 2].value += game_state[i - 1].value
                game_state[i - 1].value = 0
        for i in range(4, 17, 4):
            if game_state[i - 2].value == 0:
                game_state[i - 2].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i - 2].value == game_state[i - 1].value:
                game_state[i - 2].value += game_state[i - 1].value
                game_state[i - 1].value = 0


def move_right(game_state):
    for iter in range(3):
        for i in range(3, 16, 4):
            if game_state[i].value == 0:
                game_state[i].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i].value == game_state[i - 1].value:
                game_state[i].value += game_state[i - 1].value
                game_state[i - 1].value = 0
        for i in range(2, 15, 4):
            if game_state[i].value == 0:
                game_state[i].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i].value == game_state[i - 1].value:
                game_state[i].value += game_state[i - 1].value
                game_state[i - 1].value = 0
        for i in range(1, 14, 4):
            if game_state[i].value == 0:
                game_state[i].value = game_state[i - 1].value
                game_state[i - 1].value = 0
            elif game_state[i].value == game_state[i - 1].value:
                game_state[i].value += game_state[i - 1].value
                game_state[i - 1].value = 0
