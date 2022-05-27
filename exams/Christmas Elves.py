from collections import deque

energy = deque(int(x) for x in input().split())
materials = [int(x) for x in input().split()]
toys_made = 0
total_energy = 0
tries = 0
while energy and materials:
    current_energy = energy.popleft()
    current_materials = materials.pop()
    tries += 1
    if current_energy < 5:
        materials.append(current_materials)
    else:
        if current_energy >= current_materials:
            if tries % 3 == 0:
                current_materials *= 2
                if tries % 5 == 0:
                    if current_energy >= current_materials:
                        current_energy -= current_materials
                        total_energy += current_materials
                        energy.append(current_energy)

                elif current_energy >= current_materials:
                    toys_made += 2
                    current_energy -= current_materials
                    current_energy += 1
                    total_energy += current_materials
                    energy.append(current_energy)
                else:
                    current_energy *= 2
                    energy.append(current_energy)
                    materials.append(int(current_materials // 2))
            elif tries % 5 == 0:
                if current_energy >= current_materials:
                    current_energy -= current_materials
                    total_energy += current_materials
                    energy.append(current_energy)
            else:
                current_energy -= current_materials
                current_energy += 1
                toys_made += 1
                total_energy += current_materials
                energy.append(current_energy)

        elif current_energy < current_materials:
            current_energy *= 2
            energy.append(current_energy)
            materials.append(current_materials)
print(f'Toys: {toys_made}')
print(f'Energy: {total_energy}')
if energy:
    print(f'Elves left: {", ".join([str(x) for x in energy])}')
if materials:
    print(f'Boxes left: {", ".join([str(x) for x in materials])}')
