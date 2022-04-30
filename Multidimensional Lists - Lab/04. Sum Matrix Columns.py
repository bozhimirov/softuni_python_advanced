import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''

# sys.stdin = StringIO(test_input1)


def get_column_sums(matrix):
    column_sums = [0] * columns_count

    for row_index in range(rows_count):
        for column_index in range(columns_count):
            column_sums[column_index] += matrix[row_index][column_index]
    return column_sums


def get_column_sums2(matrix):
    column_sums = []
    for column_index in range(columns_count):
        column_sums.append(0)
        for row_index in range(rows_count):
            column_sums[-1] += matrix[row_index][column_index]

    return column_sums
# n, m
rows_count, columns_count = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows_count):
    matrix.append(
        [int(x) for x in input().split(' ')]
    )


[print(x) for x in get_column_sums2(matrix)]

