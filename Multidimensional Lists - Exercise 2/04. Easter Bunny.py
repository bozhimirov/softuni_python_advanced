import sys
from io import StringIO

test_input1 = '''8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22

'''
test_input2 = '''8
4 18 9 7 24 41 52 11
54 21 19 X 6 34 75 57
76 67 7 44 76 27 56 37
92 35 25 37 52 34 56 72
35 X 1 45 4 X 37 63
105 X B 2 12 43 5 19
48 19 35 20 32 27 42 4
73 88 78 32 37 52 X 22

'''
test_input3 = '''8
0K0KKK00
0K00KKKK
00K0000K
KKKKKK0K
K0K0000K
KK00000K
00K0K000
000K00KK
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def find_count(matrix, row, col):
    moves = [
        [row - 2, col - 1],
        [row - 2, col + 1],
        [row - 1, col - 2],
        [row - 1, col + 2],
        [row + 1, col - 2],
        [row + 1, col + 2],
        [row + 2, col - 1],
        [row + 2, col + 1],
    ]
    result = 0
    for r, c in moves:
        if 0 <= r < len(matrix) and 0 <= c < len(matrix) and matrix[r][c] == 'K':
            result += 1
    return result


size = int(input())
matrix = []
bunny_row = 0
bunny_col = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'B':
            bunny_row = row
            bunny_col = col
    matrix.append(row_elements)

directions = {
    'right': lambda r, c: (r, c + 1),
    'left': lambda r, c: (r, c - 1),
    'up': lambda r, c: (r - 1, c),
    'down': lambda r, c: (r + 1, c),
}
best_sum = float("-inf")
best_dir = ''
coordinates = []
for direction in directions:
    current_sum = 0
    row, col = directions[direction](bunny_row, bunny_col)
    current_path = []

    while 0 <= row < size and 0 <= col < size and matrix[row][col] != 'X':
        current_sum += int(matrix[row][col])
        current_path.append([row, col])
        row, col = directions[direction](row, col)

    if current_sum > best_sum and current_path:
        best_sum = current_sum
        best_dir = direction
        coordinates = current_path

print(best_dir)
print(*coordinates, sep='\n')
print(best_sum)
