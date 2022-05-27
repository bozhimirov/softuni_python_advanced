player_1, player_2 = input().split(', ')
size = 6
matrix = []
traps = []
walls = []
exits = []
exit_condition = False
trap_condition = False
sleep_condition = False
turns = 0
current_player = player_1
next_player = player_2
sleeping = []

for row in range(size):
    row_elements = input().split()
    for col in range(size):
        if row_elements[col] == "T":
            traps.append((row, col))
        elif row_elements[col] == "W":
            walls.append((row, col))
        elif row_elements[col] == "E":
            exits.append((row, col))

    matrix.append(row_elements)

while not exit_condition or not trap_condition:
    turns += 1
    command = input()[1:-1]
    command_row, command_col = int(command[0]), int(command[3])
    if turns % 2 == 0:
        current_player, next_player = player_2, player_1
        if current_player in sleeping:
            sleeping.remove(current_player)
            continue
        else:
            if (command_row, command_col) in exits:
                exit_condition = True
                print(f'{current_player} found the Exit and wins the game!')
                break
            elif (command_row, command_col) in traps:
                trap_condition = True
                print(f'{current_player} is out of the game! The winner is {next_player}')
                break
            elif (command_row, command_col) in walls:
                print(f'{current_player} hits a wall and needs to rest.')
                sleep_condition = True
                sleeping.append(current_player)
    else:
        current_player, next_player = player_1, player_2
        if current_player in sleeping:
            sleeping.remove(current_player)
            continue
        else:
            if (command_row, command_col) in exits:
                exit_condition = True
                print(f'{current_player} found the Exit and wins the game!')
                break
            elif (command_row, command_col) in traps:
                trap_condition = True
                print(f'{current_player} is out of the game! The winner is {next_player}')
                break
            elif (command_row, command_col) in walls:
                print(f'{current_player} hits a wall and needs to rest.')
                sleep_condition = True
                sleeping.append(current_player)


