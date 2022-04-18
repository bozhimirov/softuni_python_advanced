n = int(input())
best_intersection = set()
for _ in range(n):
    first_range, sec_range = input().split('-')

    first_start, first_end = [int(x) for x in first_range.split(',')]
    sec_start, sec_end = [int(x) for x in sec_range.split(',')]

    first = set(range(first_start, first_end + 1))
    second = set(range(sec_start, sec_end + 1))

    current_intersection = first.intersection(second)
    if len(current_intersection) > len(best_intersection):
        best_intersection = current_intersection

print(f'Longest intersection is [{", ".join([str(x) for x in best_intersection])}] with length {len(best_intersection)}')
