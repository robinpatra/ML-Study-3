def show_board(b):
    print("---------")
    print("|", b[0][0], b[0][1], b[0][2], "|")
    print("|", b[1][0], b[1][1], b[1][2], "|")
    print("|", b[2][0], b[2][1], b[2][2], "|")
    print("---------")


def translate_coordinate(_x, _y):
    # x=1 j=0, x=2 j=1, x=3 j=2
    # y=1 i=2, y=2 i=1, y=3 i=0
    return 3 - _y, _x - 1


def check_winner(b):
    lines = [
        # horizontal
        [b[0][0] != "_" and b[0][0] == b[0][1] and b[0][1] == b[0][2], b[0][0]],
        [b[1][0] != "_" and b[1][0] == b[1][1] and b[1][1] == b[1][2], b[1][0]],
        [b[2][0] != "_" and b[2][0] == b[2][1] and b[2][1] == b[2][2], b[2][0]],
        # vertical
        [b[0][0] != "_" and b[0][0] == b[1][0] and b[1][0] == b[2][0], b[0][0]],
        [b[0][1] != "_" and b[0][1] == b[1][1] and b[1][1] == b[2][1], b[0][1]],
        [b[0][2] != "_" and b[0][2] == b[1][2] and b[1][2] == b[2][2], b[0][2]],
        # diagonal
        [b[0][0] != "_" and b[0][0] == b[1][1] and b[1][1] == b[2][2], b[0][0]],
        [b[0][2] != "_" and b[0][2] == b[1][1] and b[1][1] == b[2][0], b[0][2]]
    ]
    return [player for [result, player] in lines if result]


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


board = [
    ["_", "_", "_"],
    ["_", "_", "_"],
    ["_", "_", "_"]
]
is_x_move = True
move_count = 0

show_board(board)
while True:
    new_move = input("Enter the coordinates: > ")
    message, coordinates = coordinate_check(new_move)
    if message == "OK":
        x, y = coordinates
        i, j = translate_coordinate(x, y)
        if board[i][j] == "_":
            board[i][j] = "X" if is_x_move else "O"
            is_x_move = not is_x_move
            move_count += 1
            show_board(board)
            winner = check_winner(board)
            if len(winner) > 0:
                print(winner[0], "wins")
                break
            elif move_count == 9:
                print("Draw")
                break
        else:
            message = "This cell is occupied! Choose another one!"
    if message != "OK":
        print(message)
