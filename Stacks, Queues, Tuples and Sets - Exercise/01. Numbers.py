first_set = set([int(x) for x in input().split()])
sec_set = set([int(x) for x in input().split()])
n = int(input())
for _ in range(n):
    command = input().split()
    if command[0] == "Add":
        if command[1] == "First":
            [first_set.add(int(x)) for x in command[2:]]
        else:
            [sec_set.add(int(x)) for x in command[2:]]
    elif command[0] == "Remove":
        if command[1] == "First":
            first_set = first_set.difference([int(x) for x in command[2:]])
        else:
            sec_set = sec_set.difference([int(x) for x in command[2:]])

    else:
        print(first_set.issubset(sec_set) or sec_set.issubset(first_set))


print(sep=', ', *sorted(first_set))
print(*sorted(sec_set), sep=', ')
