n, m = [int(x) for x in input().split(', ')]
matrix = []

matrix_sum = 0
for _ in range(n):
    row = [int(x) for x in input().split(', ')]
    matrix.append(row)
    matrix_sum += sum(row)
print(matrix_sum)
print(matrix)
