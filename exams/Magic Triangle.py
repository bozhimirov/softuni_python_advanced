def get_magic_triangle(param):
    triangle = [[1], [1, 1]]

    for row_index in range(2, param):
        triangle.append([])
        triangle[-1].append(1)
        for col_index in range(1, row_index):
            left = triangle[row_index - 1][col_index - 1]
            right = triangle[row_index - 1][col_index]
            triangle[-1].append(
                left + right
            )
        triangle[-1].append(1)
    return triangle
