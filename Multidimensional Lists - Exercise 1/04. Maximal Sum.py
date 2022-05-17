rows, cols = [int(x) for x in input().split()]
matrix = []
for _ in range(rows):
    matrix.append([int(x) for x in input().split()])
biggest_sum = float('-inf')
started_row = 0
started_column = 0
for row in range(rows - 2):
    for col in range(cols - 2):
        current_sum = matrix[row][col] + matrix[row][col + 1] + matrix[row][col + 2] + matrix[row + 1][col] + matrix[row + 1][col + 1] + matrix[row + 1][col + 2] + matrix[row + 2][col] + matrix[row + 2][col + 1] + matrix[row + 2][col + 2]
        if current_sum > biggest_sum:
            biggest_sum = current_sum
            started_row = row
            started_column = col

print(f'Sum = {biggest_sum}')
print(f'{matrix[started_row][started_column]} {matrix[started_row][started_column + 1]} {matrix[started_row][started_column + 2]}')
print(f'{matrix[started_row + 1][started_column]} {matrix[started_row + 1][started_column + 1]} {matrix[started_row + 1][started_column + 2]}')
print(f'{matrix[started_row + 2][started_column]} {matrix[started_row + 2][started_column + 1]} {matrix[started_row + 2][started_column + 2]}')
