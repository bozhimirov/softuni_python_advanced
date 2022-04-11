from collections import deque

pump_count = int(input())
pumps = deque()
for _ in range(pump_count):
    pumps.append([int(x) for x in input().split()])

for attempt in range(pump_count):
    trunk = 0
    failed = False
    for petrol, distance in pumps:
        trunk = trunk + petrol - distance
        if trunk < 0:
            failed = True
            break

    if failed:
        pumps.append(pumps.popleft())
    else:
        print(attempt)
        break