from collections import deque

expression = input().split()
numbers = deque()
for element in expression:
    if element in "+-*/":
        while len(numbers) > 1:
            first = numbers.popleft()
            second = numbers.popleft()
            result = 0
            if element == "-":
                result = first - second
            elif element == "+":
                result = first + second
            elif element == "*":
                result = first * second
            elif element == "/":
                result = first // second
            numbers.appendleft(result)
    else:
        numbers.append(int(element))

print(numbers.popleft())

