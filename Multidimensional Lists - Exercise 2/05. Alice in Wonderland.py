import sys
from io import StringIO

test_input1 = '''5
. A . . 1
R . 2 . .
4 7 . 1 .
. . . 2 .
. 3 . . .
down
right
left
down
up
left

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


def get_next_pos(row, col, direction):
    if direction == 'up':
        return row - 1, col
    if direction == 'down':
        return row + 1, col
    if direction == 'left':
        return row, col - 1
    if direction == 'right':
        return row, col + 1


size = int(input())
matrix = []
alice_row = 0
alice_col = 0

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == 'A':
            alice_row = row
            alice_col = col
    matrix.append(row_elements)

tea_bags = 0

while tea_bags < 10:
    matrix[alice_row][alice_col] = "*"
    direction = input()
    next_row, next_col = get_next_pos(alice_row, alice_col, direction)

    if next_row < 0 or next_col < 0 or next_row >= size or next_col >= size:
        break
    alice_row, alice_col = next_row, next_col
    if matrix[alice_row][alice_col] == '.' or matrix[alice_row][alice_col] == '*':
        continue
    if matrix[alice_row][alice_col] == 'R':
        break
    tea_bags += int(matrix[alice_row][alice_col])
matrix[alice_row][alice_col] = "*"
if tea_bags >= 10:
    print('She did it! She went to the party.')
else:
    print("Alice didn't make it to the tea party.")
for row in matrix:
    print(*row, sep=' ')


