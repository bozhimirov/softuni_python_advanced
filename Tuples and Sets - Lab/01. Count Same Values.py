numbers_string = input()
occurrence_counts = {}

numbers = [float(x) for x in numbers_string.split(' ')]
for number in numbers:
    if number not in occurrence_counts:
        occurrence_counts[number] = 0
    occurrence_counts[number] += 1
for number, count in occurrence_counts.items():
    print(f'{number:.1f} - {count} times')