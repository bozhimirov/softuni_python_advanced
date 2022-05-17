rows, cols = [int(x) for x in input().split()]
word = input()

idx = 0
for row in range(rows):
    elements = [None] * cols
    start, end, step = (0, cols, 1) if row % 2 == 0 else (cols - 1, -1, -1)
    for col in range(start, end, step):
        elements[col] = word[idx % len(word)]
        idx += 1
    print(''.join(elements))
