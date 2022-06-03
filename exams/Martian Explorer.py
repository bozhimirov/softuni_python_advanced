size = 6
matrix = []
rover_row = None
rover_col = None
water_deposit = []
metal_deposit = []
concrete_deposit = []
rocks = []

for row in range(size):
    current_row = [x for x in input().split(' ')]
    for col in range(len(current_row)):
        if current_row[col] == 'R':
            rocks.append((row, col))
        elif current_row[col] == 'E':
            rover_row, rover_col = row, col
    matrix.append(current_row)

commands = input().split(', ')


def change_position(rrow, ccol, direction):
    if direction == "up":
        nrow, ccol = rrow - 1, ccol
        if rrow - 1 < 0:
            nrow = size - 1
        return nrow, ccol
    elif direction == 'down':
        nrow, ccol = rrow + 1, ccol
        if rrow + 1 > size - 1:
            nrow = 0
        return nrow, ccol
    elif direction == 'left':
        nrow, ncol = rrow - 1, (ccol - 1)
        if ccol - 1 < 0:
            ncol = size - 1
        return rrow, ncol

    elif direction == 'right':
        rrow, ncol = rrow, (ccol + 1)
        if ccol + 1 > size - 1:
            ncol = 0
        return rrow, ncol


c_row, c_col = rover_row, rover_col
for command in commands:
    c_row, c_col = change_position(c_row, c_col, command)
    if (c_row, c_col) not in rocks:
        if matrix[c_row][c_col] == 'W':
            water_deposit.append((c_row, c_col))
            print(f'Water deposit found at ({c_row}, {c_col})')
        elif matrix[c_row][c_col] == "C":
            concrete_deposit.append((c_row, c_col))
            print(f'Concrete deposit found at ({c_row}, {c_col})')
        elif matrix[c_row][c_col] == 'M':
            metal_deposit.append((c_row, c_col))
            print(f'Metal deposit found at ({c_row}, {c_col})')
    else:
        print(f'Rover got broken at ({c_row}, {c_col})')
        break
if water_deposit and concrete_deposit and metal_deposit:
    print('Area suitable to start the colony.')
else:
    print('Area not suitable to start the colony.')


