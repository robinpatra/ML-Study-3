def input_two_matrices():
    a = []
    b = []
    a_row, a_col = [int(x) for x in input("Enter size of first matrix: > ").split()]
    print("Enter first matrix:")
    for _ in range(a_row):
        a.append([float(x) for x in input("> ").split()])
    b_row, b_col = [int(x) for x in input("Enter size of second matrix: > ").split()]
    print("Enter second matrix:")
    for _ in range(b_row):
        b.append([float(x) for x in input("> ").split()])
    return a, b


def input_single_matrix():
    a = []
    a_row, a_col = [int(x) for x in input("Enter size of matrix: > ").split()]
    for _ in range(a_row):
        a.append([float(x) for x in input("> ").split()])
    return a


def print_matrix(matrix):
    print("The result is:")
    for row in matrix:
        print(" ".join([str(x) for x in row]))


def add_matrices():
    a, b = input_two_matrices()

    def add(_a, _b):
        m = len(_a)
        n = len(_a[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = _a[i][j] + _b[i][j]
        return result

    if len(a) == len(b) and len(a[0]) == len(b[0]):
        added_matrix = add(a, b)
        print_matrix(added_matrix)
    else:
        print("ERROR")


def multiply_matrix_by_a_constant():
    a = input_single_matrix()
    scalar = float(input("Enter constant: > "))

    def scalar_multiplication(_a, _scalar):
        m = len(_a)
        n = len(_a[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                result[i][j] = _a[i][j] * _scalar
        return result

    scalar_multiplication_result_matrix = scalar_multiplication(a, scalar)
    print_matrix(scalar_multiplication_result_matrix)


def multiply_matrices():
    a, b = input_two_matrices()

    def multiply(_a, _b):
        m = len(_a)
        n = len(_b[0])
        result = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                _row = _a[i]
                count = 0
                for index, value in enumerate(_row):
                    count += value * _b[index][j]
                result[i][j] = count
        return result

    if len(a[0]) == len(b):
        multiplied_matrix = multiply(a, b)
        print_matrix(multiplied_matrix)
    else:
        print("ERROR")


def get_zero_transpose_matrix(matrix):
    m = len(matrix)
    n = len(matrix[0])
    matrix_t = [[0.0] * m for _ in range(n)]
    return matrix_t, n, m


def main_diagonal_transpose():
    a = input_single_matrix()
    a_t, m_t, n_t = get_zero_transpose_matrix(a)
    for i in range(m_t):
        for j in range(n_t):
            a_t[i][j] = a[j][i]
    print_matrix(a_t)


def side_diagonal_transpose():
    a = input_single_matrix()
    a_t, m_t, n_t = get_zero_transpose_matrix(a)
    for i in range(m_t):
        for j in range(n_t):
            old_i = n_t - 1 - j
            old_j = m_t - 1 - i
            a_t[i][j] = a[old_i][old_j]
    print_matrix(a_t)


def vertical_diagonal_transpose():
    a = input_single_matrix()
    a_t = [reversed(row) for row in a]
    print_matrix(a_t)


def horizontal_diagonal_transpose():
    a = input_single_matrix()
    a_t = reversed(a)
    print_matrix(a_t)


def transpose_matrix():
    print("1. Main diagonal")
    print("2. Side diagonal")
    print("3. Vertical line")
    print("4. Horizontal line")
    transpose_choice = input("Your choice: > ")
    if transpose_choice == "1":
        main_diagonal_transpose()
    elif transpose_choice == "2":
        side_diagonal_transpose()
    elif transpose_choice == "3":
        vertical_diagonal_transpose()
    elif transpose_choice == "4":
        horizontal_diagonal_transpose()


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
    print("4. Transpose matrix")
    print("0. Exit")
    choice = input("Your choice: > ")
    if choice == "0":
        break
    if choice == "1":
        add_matrices()
    elif choice == "2":
        multiply_matrix_by_a_constant()
    elif choice == "3":
        multiply_matrices()
    elif choice == "4":
        transpose_matrix()
    print()
