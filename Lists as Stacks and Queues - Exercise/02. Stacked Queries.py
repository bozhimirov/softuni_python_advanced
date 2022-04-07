stack = []
number = int(input())
for _ in range(number):
    command_extended = input().split()
    command = command_extended[0]

    if command == "1":
        num = command_extended[1]
        stack.append(num)
    elif command == "2" and stack:
        stack.pop()
    elif command == "3" and stack:
        print(max(stack))
    elif command == "4" and stack:
        print(min(stack))

rev_stack = []
while stack:
    rev_stack.append(stack.pop())

print(', '.join(rev_stack))



