from collections import deque

working_bees = deque([int(x) for x in input().split()])
nectar = [int(x) for x in input().split()]
symbols = deque(input().split())
result = 0
while working_bees and nectar:
    first_bee = working_bees[0]
    current_nectar = nectar.pop()
    if current_nectar < first_bee:
        continue

    working_bees.popleft()
    operator = symbols.popleft()

    if operator == "+":
        result += abs(first_bee + current_nectar)
    elif operator == "-":
        result += abs(first_bee - current_nectar)
    elif operator == "*":
        result += abs(first_bee * current_nectar)
    elif operator == "/":
        result += abs(first_bee / current_nectar)
print(f'Total honey made: {result}')
if working_bees:
    print(f"Bees left: {', '.join(str(x) for x in working_bees)}")
if nectar:
    print(f"Nectar left: {', '.join(str(x) for x in nectar)}")



