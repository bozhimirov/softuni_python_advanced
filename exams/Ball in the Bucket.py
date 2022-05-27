matrix = []
buckets = []
points = 0

for row in range(6):
    row_elements = input().split()
    for col in range(6):
        if row_elements[col] == "B":
            bucket_row, bucket_col = row, col
            buckets.append((bucket_row, bucket_col))

    matrix.append(row_elements)

for count in range(3):
    coordinates = input()
    naked_coordinates = coordinates[1:-1]
    row_coordinates, col_coordinates = naked_coordinates.split(', ')
    coord = [(int(row_coordinates), int(col_coordinates))]
    if coord[0] in buckets:
        for i in range(len(buckets)):
            if buckets[i] == coord[0]:
                buckets.pop(i)
                break
        for c in range(6):
            matrix[int(row_coordinates)][int(col_coordinates)] = 0
            if matrix[c][int(col_coordinates)] != "B":
                points += int(matrix[c][int(col_coordinates)])

if points < 100:
    print(f"Sorry! You need {100 - points} points more to win a prize.")
elif 100 <= points <= 199:
    print(f"Good job! You scored {points} points, and you've won Football.")
elif 200 <= points <= 299:
    print(f"Good job! You scored {points} points, and you've won Teddy Bear.")
elif 300 <= points:
    print(f"Good job! You scored {points} points, and you've won Lego Construction Set.")


