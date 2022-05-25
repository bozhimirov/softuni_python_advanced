from collections import deque


def calculate_sum(current_sum):
    if 400 <= current_sum <= 499:
        if "Diamond Jewellery" not in crafted_gifts:
            crafted_gifts["Diamond Jewellery"] = 1
        else:
            crafted_gifts["Diamond Jewellery"] += 1
    elif 300 <= current_sum <= 399:
        if "Gold" not in crafted_gifts:
            crafted_gifts["Gold"] = 1
        else:
            crafted_gifts["Gold"] += 1
    elif 200 <= current_sum <= 299:
        if "Porcelain Sculpture" not in crafted_gifts:
            crafted_gifts["Porcelain Sculpture"] = 1
        else:
            crafted_gifts["Porcelain Sculpture"] += 1
    elif 100 <= current_sum <= 199:
        if "Gemstone" not in crafted_gifts:
            crafted_gifts["Gemstone"] = 1
        else:
            crafted_gifts["Gemstone"] += 1


materials = [int(x) for x in input().split()]
magic_levels = deque(int(x) for x in input().split())

crafted_gifts = {}
success = False

while materials and magic_levels:
    current_material = materials.pop()
    current_magic_level = magic_levels.popleft()
    current_sum = current_material + current_magic_level
    calculate_sum(current_sum)
    if current_sum < 100:
        if current_sum % 2 == 0:
            new_sum = (current_material * 2) + (current_magic_level * 3)
            calculate_sum(new_sum)
        else:
            new_sum = current_sum * 2
            calculate_sum(new_sum)
    elif current_sum > 499:
        new_sum = current_sum / 2
        calculate_sum(new_sum)
if "Gemstone" in crafted_gifts and "Porcelain Sculpture" in crafted_gifts:
    success = True
if "Gold" in crafted_gifts and "Diamond Jewellery" in crafted_gifts:
    success = True

if success:
    print('The wedding presents are made!')
else:
    print('Aladdin does not have enough wedding presents.')
if materials:
    print(f'Materials left: {", ". join(str(x) for x in materials)}')
if magic_levels:
    print(f'Magic left: {", ". join(str(x) for x in magic_levels)}')
for present, amount in sorted(crafted_gifts.items()):
    print(f'{present}: {amount}')


