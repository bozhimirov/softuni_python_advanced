from collections import deque

water_quantity = int(input())
command = input()
queue = deque()
while command != 'Start':
    queue.append(command)
    command = input()

command2 = input()
while command2 != 'End':
    command2 = command2.split(' ')
    if command2[0] == 'refill':
        water_quantity += int(command2[1])
    else:
        command2 = int(command2[0])
        if (water_quantity - command2) < 0:
            print(f'{queue.popleft()} must wait')
        else:
            print(f'{queue.popleft()} got water')
            water_quantity -= int(command2)
    command2 = input()
print(f'{water_quantity} liters left')
