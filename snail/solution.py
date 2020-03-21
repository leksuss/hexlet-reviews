def snail(matrix):
    x = y = 0
    snail_line = []
    matrix_size = len(matrix[0])

    for num in range(1, matrix_size ** 2 + 1):
        snail_line.append(matrix[x][y])
        if x <= y + 1 and x + y < matrix_size - 1:
            y += 1
        elif x < y and x + y >= matrix_size - 1:
            x += 1
        elif x >= y and x + y > matrix_size - 1:
            y -= 1
        elif x > y + 1 and x + y <= matrix_size - 1:
            x -= 1

    return snail_line


def snail2(matrix):
    snail_line = []
    steps = (0, 1), (1, 0), (0, -1), (-1, 0)
    change_way = 0
    x, y = 0, 0
    shift_x, shift_y = 0, 1
    visited = object()
    matrix_size = len(matrix[0])

    for num in range(1, matrix_size ** 2 + 1):
        snail_line.append(matrix[x][y])
        matrix[x][y] = visited
        if (x + shift_x == matrix_size or
                y + shift_y == matrix_size or
                matrix[x + shift_x][y + shift_y] == visited):
            change_way = (change_way + 1) % 4
            shift_x, shift_y = steps[change_way][0], steps[change_way][1]
        x += shift_x
        y += shift_y

    return snail_line
