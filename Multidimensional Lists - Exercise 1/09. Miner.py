import sys
from collections import deque
from io import StringIO

test_input1 = '''5
up right right up right
* * * c *
* * * e *
* * c * *
s * * c *
* * c * *

'''
test_input2 = '''4
up right right right down
* * * e
* * c *
* s * c
* * * *
'''
test_input3 = '''6
left left down right up left left down down down
* * * * * *
e * * * c *
* * c s * *
* * * * * *
c * * * c *
* * c * * *
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)
# sys.stdin = StringIO(test_input3)


def movement(row, col, commands):
    current_command = commands.popleft()
    if current_command == "left":
        return row, col - 1
    elif current_command == "right":
        return row, col + 1
    elif current_command == "up":
        return row - 1, col
    elif current_command == "down":
        return row + 1, col


def is_outside(row, col, size):
    return row < 0 or col < 0 or row >= size or col >= size


size = int(input())
matrix = []
commands = deque(input().split())

for _ in range(size):
    matrix.append(input().split())
start_position = 0
end_position = 0
coal_position = list()

coal_count = 0

for i in range(size):
    for j in range(size):
        if matrix[i][j] == "s":
            start_position = f'{i} {j}'
        if matrix[i][j] == "e":
            end_position = f'{i} {j}'
        if matrix[i][j] == "c":
            coal_position.append(f'{i} {j}')
            coal_count += 1
while commands:
    start_position_sep = [int(x) for x in start_position.split()]
    start_row, start_col = [x for x in start_position_sep]
    new_row, new_col = movement(start_row, start_col, commands)
    if is_outside(new_row, new_col, size):
        continue
    start_position = f'{new_row} {new_col}'
    if start_position == end_position:
        print(f"Game over! ({new_row}, {new_col})")
        break
    elif start_position in coal_position:
        if coal_count > 0:
            coal_count -= 1
            if coal_count == 0:
                print(f'You collected all coal! ({new_row}, {new_col})')
                break
            else:
                coal_position.remove(start_position)
    elif not commands:
        print(f'{coal_count} pieces of coal left. ({new_row}, {new_col})')



