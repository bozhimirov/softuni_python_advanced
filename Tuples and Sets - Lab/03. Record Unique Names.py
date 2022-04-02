n = int(input())
name_set = set(input() for _ in range(n))
[print(name) for name in name_set]