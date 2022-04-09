box = [int(x) for x in input().split()]
capacity = int(input())

current_capacity = capacity
rack_counter = 1
while box:
    clothing = box[-1]
    if clothing > current_capacity:
        rack_counter += 1
        current_capacity = capacity
    else:
        current_capacity -= clothing
        box.pop()
print(rack_counter)