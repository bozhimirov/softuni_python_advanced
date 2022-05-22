size = int(input())
matrix = []
for _ in range(size):
    matrix.append([int(x) for x in input().split()])

command = input().split()
while command[0] != 'END':
    row, col, value = [int(x) for x in command[1:]]
    if row < 0 or col < 0 or row >= size or col >= size:
        print('Invalid coordinates')
        command = input().split()
        continue
    if command[0] == "Add":
        matrix[row][col] += value
    elif command[0] == "Subtract":
        matrix[row][col] -= value
    command = input().split()

for row in matrix:
    print(*row, sep=' ')
