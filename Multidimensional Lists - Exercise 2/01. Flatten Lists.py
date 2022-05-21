string = input().split('|')
result = []
for index in range(len(string) - 1, -1, -1):
    current_elements = string[index].strip().split()
    result.extend(current_elements)
print(' '.join(result))
