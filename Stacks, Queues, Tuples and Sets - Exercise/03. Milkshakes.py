from collections import deque

chocolates = [int(x) for x in input().split(', ')]
milks = deque([int(x) for x in input().split(', ')])
milk_shakes = 0
condition = False
while chocolates and milks and milk_shakes < 5:
    cho = chocolates.pop()
    mlk = milks.popleft()

    if cho <= 0 and mlk <= 0:
        continue
    if cho <= 0:
        milks.appendleft(mlk)
        continue
    if mlk <= 0:
        chocolates.append(cho)
        continue

    if cho == mlk:
        milk_shakes += 1
    else:
        chocolates.append(cho - 5)
        milks.append(mlk)

if milk_shakes == 5:
    print("Great! You made all the chocolate milkshakes needed!")
else:
    print("Not enough milkshakes.")

if chocolates:
    print(f"Chocolate: {', '.join([str(x) for x in chocolates])}")
else:
    print("Chocolate: empty")

if milks:
    print(f'Milk: {", ".join([str(x) for x in milks])}')
else:
    print("Milk: empty")

