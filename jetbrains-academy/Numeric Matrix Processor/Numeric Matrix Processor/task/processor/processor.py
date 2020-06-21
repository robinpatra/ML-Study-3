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
        print("The result is:")
        for row in added_matrix:
            print(" ".join([str(x) for x in row]))
    else:
        print("ERROR")


def multiply_matrix_by_a_constant():
    a = []

    a_row, a_col = [int(x) for x in input("Enter size of matrix: > ").split()]
    for _ in range(a_row):
        a.append([float(x) for x in input("> ").split()])
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
    print("The result is:")
    for row in scalar_multiplication_result_matrix:
        print(" ".join([str(x) for x in row]))


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
        print("The result is:")
        for row in multiplied_matrix:
            print(" ".join([str(x) for x in row]))
    else:
        print("ERROR")


while True:
    print("1. Add matrices")
    print("2. Multiply matrix by a constant")
    print("3. Multiply matrices")
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
    print()
