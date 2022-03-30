from collections import deque

# kids_string = 'George Peter Michael William Thomas'
# tosses_count_string = '1'

kids = deque(input().split(' '))
tosses_count = int(input())

current_count = 0
while len(kids) > 1:
    current_count += 1
    kid = kids.popleft()
    if current_count < tosses_count:
        kids.append(kid)
    else:
        print(f'Removed {kid}')
        current_count = 0
kid = kids.popleft()
print(f'Last is {kid}')
