# write your code here
# print("""
# X O X
# O X O
# X X O
# """)


def print_game(c):
    print("---------")
    print("|", c[0], c[1], c[2], "|")
    print("|", c[3], c[4], c[5], "|")
    print("|", c[6], c[7], c[8], "|")
    print("---------")


def check_winner(c):
    lines = [
        # horizontal
        [c[0] == c[1] and c[1] == c[2], c[0]],
        [c[3] == c[4] and c[4] == c[5], c[3]],
        [c[6] == c[7] and c[7] == c[8], c[6]],
        # vertical
        [c[0] == c[3] and c[3] == c[6], c[0]],
        [c[1] == c[4] and c[4] == c[7], c[1]],
        [c[2] == c[5] and c[5] == c[8], c[2]],
        # diagonal
        [c[0] == c[4] and c[4] == c[8], c[0]],
        [c[2] == c[4] and c[4] == c[6], c[2]]
    ]
    return [player for [result, player] in lines if result == True]


def sanity_check(result):
    s = set(result)
    return len(s) == 1


cells = input("Enter cells:")
# cells = "XXXOO__O_"  # X wins
# cells = "XOXOXOXXO"  # X wins
# cells = "XOOOXOXXO"  # O wins
# cells = "XOXOOXXXO"  # Draw
# cells = "XO_OOX_X_"  # Game not finished
# cells = "XO_XO_XOX"  # Impossible
# cells = "_O_X__X_X"  # Impossible
# cells = "_OOOO_X_X"  # Impossible
print_game(cells)

x_count = 0
o_count = 0
empty_count = 0

for cell in cells:
    if cell == 'X':
        x_count += 1
    elif cell == 'O':
        o_count += 1
    else:
        empty_count += 1

if abs(x_count - o_count) > 1:
    print("Impossible")
else:
    winner = check_winner(cells)
    if len(winner) == 0:
        if x_count + o_count == 9:
            print("Draw")
        else:
            print("Game not finished")
    else:
        if sanity_check(winner):
            print(winner[0], "wins")
        else:
            print("Impossible")
