def print_hi(source):
    a = 0
    for i in range(n):
        for j in range(n - 3):
            pre_result_hor = source[i][j] * source[i][j + 1] * \
                             source[i][j + 2] * source[i][j + 3]

            pre_result_vert = source[j][i] * source[j + 1][i] * \
                              source[j + 2][i] * source[j + 3][i]

            if pre_result_vert > pre_result_hor:
                a = pre_result_vert
            else:
                a = pre_result_hor

    for d in range(n - 3):
        for c in range(n - 3):
            pre_result_diag = source[d][c] * source[d + 1][c + 1] * \
                              source[d + 2][c + 2] * source[d + 3][c + 3]
            if pre_result_diag > a:
                a = pre_result_diag

    for x in range(n - 3):
        for y in range(n - 1, 2, -1):
            pre_result_alt_diag = source[x][y] * source[x + 1][y - 1] * \
                                  source[x + 2][y - 2] * source[x + 3][y - 3]
            if pre_result_alt_diag > a:
                a = pre_result_alt_diag
    print(a)


if __name__ == '__main__':
    n = int(input('число строк: '))
    table = []
    for i in range(n):
        table.append(list(map(int, input().split())))
    print_hi(table)
