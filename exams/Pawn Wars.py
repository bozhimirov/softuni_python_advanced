def find_player_position(matrix, player):
    for (row_index, row) in enumerate(matrix):
        if player in row:
            return (row_index, row.index(player))
    return (None, None)


def get_chess_position(row, column):
    row_names = [8, 7, 6, 5, 4, 3, 2, 1]
    column_names = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    return row_names[row], column_names[column]


rows_count = 8
columns_count = 8

matrix = [input().split(' ') for _ in range(rows_count)]
current_player = 'w'
other_player = 'b'
current_player_position = find_player_position(matrix, "w")
other_player_position = find_player_position(matrix, "b")

current_delta = -1
other_delta = +1

is_capture = False
is_queen = False

while not is_queen and not is_capture:
    (current_player_row, current_player_column) = current_player_position
    (other_player_row, other_player_column) = other_player_position

    current_player_row += current_delta
    current_player_position = (current_player_row, current_player_column)

    if current_player_row == other_player_row and abs(current_player_column - other_player_column) == 1:
        is_capture = True
        current_player_position = (current_player_row, other_player_column)
    elif current_player_row in (0, rows_count - 1):
        is_queen = True
    else:
        current_player_position, other_player_position = other_player_position, current_player_position
        current_delta, other_delta = other_delta, current_delta
        current_player, other_player = other_player, current_player


player = 'White' if current_player == 'w' else 'Black'
(row_name, column_name) = get_chess_position(*current_player_position)
position_name = f'{column_name}{row_name}'
if is_capture:
    print(f'Game over! {player} win, capture on {position_name}.')
elif is_queen:
    print(f'Game over! {player} pawn is promoted to a queen at {column_name}{row_name}.')
