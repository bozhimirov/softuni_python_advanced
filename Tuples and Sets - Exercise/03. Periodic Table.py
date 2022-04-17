count = int(input())
elements_set = set()
for _ in range(count):
    elements = set(input().split())
    elements_set = elements_set.union(elements)
print(*elements_set, sep='\n')

