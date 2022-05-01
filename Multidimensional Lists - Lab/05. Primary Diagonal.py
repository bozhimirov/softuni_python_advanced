import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''

# sys.stdin = StringIO(test_input1)
def primary_diagonal(matrix):
    the_sum = 0
    n= len(matrix)
    # NxN - very bad
    # for r in range(n):
    #     for c in range(n):
    #         if r == c:
    #             the_sum += matrix[r][c]


    # for i in range(n):
    #     the_sum ++ matrix[i][i]
    # return the_sum

    return sum(matrix[i][i] for i in range(n))


def secondary_diagonal(matrix):
    n = len(matrix)
    return sum(matrix[i][n - i - 1] for i in range(n))


n = int(input())

matrix = []

for _ in range(n):
    matrix.append(
        [int(x) for x in input().split(' ')]
    )
print(primary_diagonal(matrix))