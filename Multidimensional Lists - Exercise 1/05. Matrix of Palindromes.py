rows, cols = [int(x) for x in input().split()]
matrix = []
for i in range(rows):
    list = []
    for j in range(cols):
        first_last = 97 + i
        middle = 97 + i + j
        list.append(f'{chr(first_last)}{chr(middle)}{chr(first_last)}')
    matrix.append(list)
for row in range(len(matrix)):
    print(' '.join(x for x in matrix[row]))