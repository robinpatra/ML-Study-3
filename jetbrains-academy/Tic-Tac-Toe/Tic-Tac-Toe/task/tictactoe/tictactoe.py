def show_cells(c):
    print("---------")
    print("|", c[0], c[1], c[2], "|")
    print("|", c[3], c[4], c[5], "|")
    print("|", c[6], c[7], c[8], "|")
    print("---------")


def translate_coordinate(_x, _y):
    # this is ugly, but quick and dirty
    if _x == 1:
        if _y == 1:
            return 6
        elif _y == 2:
            return 3
        else:
            return 0
    elif _x == 2:
        if _y == 1:
            return 7
        elif _y == 2:
            return 4
        else:
            return 1
    else:
        if _y == 1:
            return 8
        elif _y == 2:
            return 5
        else:
            return 2


def check_winner(c):
    lines = [
        # horizontal
        [c[0] != "_" and c[0] == c[1] and c[1] == c[2], c[0]],
        [c[3] != "_" and c[3] == c[4] and c[4] == c[5], c[3]],
        [c[6] != "_" and c[6] == c[7] and c[7] == c[8], c[6]],
        # vertical
        [c[0] != "_" and c[0] == c[3] and c[3] == c[6], c[0]],
        [c[1] != "_" and c[1] == c[4] and c[4] == c[7], c[1]],
        [c[2] != "_" and c[2] == c[5] and c[5] == c[8], c[2]],
        # diagonal
        [c[0] != "_" and c[0] == c[4] and c[4] == c[8], c[0]],
        [c[2] != "_" and c[2] == c[4] and c[4] == c[6], c[2]]
    ]
    return [player for [result, player] in lines if result]


def winner_sanity_check(result):
    s = set(result)
    return len(s) == 1


def coordinate_check(input_string):
    string_coordinates = input_string.split(" ")
    if len(string_coordinates) != 2:
        return "You should enter numbers!", None
    try:
        int_coordinate = [int(n) for n in string_coordinates]
        if 1 <= int_coordinate[0] <= 3 and 1 <= int_coordinate[1] <= 3:
            return "OK", int_coordinate
        else:
            return "Coordinates should be from 1 to 3!", None
    except ValueError:
        return "You should enter numbers!", None


def game(cells):
    x_count = 0
    o_count = 0

    for cell in cells:
        if cell == 'X':
            x_count += 1
        elif cell == 'O':
            o_count += 1

    if abs(x_count - o_count) > 1:
        print("Impossible")
        return True
    else:
        winner = check_winner(cells)
        if len(winner) == 0:
            if x_count + o_count == 9:
                print("Draw")
                return True
            else:
                return False
        else:
            if winner_sanity_check(winner):
                print(winner[0], "wins")
            else:
                print("Impossible")
            return True


board = input("Enter cells: > ")
show_cells(board)
is_finished = game(board)

if not is_finished:
    while True:
        new_move = input("Enter the coordinates: > ")
        message, coordinates = coordinate_check(new_move)
        if message == "OK":
            x, y = coordinates
            index = translate_coordinate(x, y)
            if board[index] == "_":
                board = board[:index] + "X" + board[index + 1:]
                show_cells(board)
                break
            else:
                message = "This cell is occupied! Choose another one!"
        print(message)

