import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''
test_input2 = '''2, 4
10 11 12 13
14 15 16 17
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

rows_count, columns_count = [int(x) for x in input().split(', ')]
matrix = []

for _ in range(rows_count):
    matrix.append(
        [int(x) for x in input().split(', ')]
    )
    biggest_sum = 0
    big_submatrix = []
for i in range(0, rows_count - 1):
    for j in range(0, columns_count - 1):
        current_sum = matrix[i][j] + matrix[i][j+1] + matrix[i+1][j] + matrix[i+1][j+1]
        submatrix = [matrix[i][j], matrix[i][j+1]],  [matrix[i+1][j],  matrix[i+1][j+1]]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            big_submatrix = submatrix
for rows in range(2):
    print(' '.join(str(x) for x in big_submatrix[rows]))

print(biggest_sum)
