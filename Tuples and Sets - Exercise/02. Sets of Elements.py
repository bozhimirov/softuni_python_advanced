n, m = [int(x) for x in input().split()]
set1 = set()
set2 = set()

for _ in range(n):
    set1.add(int(input()))
for _ in range(m):
    set2.add(int(input()))

result = set1.intersection(set2)
for num in result:
    print(num)

