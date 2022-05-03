import sys
from io import StringIO

test_input1 = '''3
11 2 4
4 5 6
10 8 -12
'''

# sys.stdin = StringIO(test_input1)


def find_symbol(matrix, symbol):

    for row_index in range(n):
        for col_index in range(n):
            if matrix[row_index][col_index] == symbol:
                return row_index, col_index
    return None


n = int(input())

matrix = [list(input()) for _ in range(n)]
symbol = input()
# is_found = False
# for row_index in range(n):
#     if is_found:
#         break
#     for col_index in range(n):
#         if matrix[row_index][col_index] == symbol:
#             is_found = True
#             print(f'{row_index}, {col_index}')
#             break
# if not is_found:
#     print(f'{symbol} does not occur in the matrix')

result = find_symbol(matrix, symbol)

if result:
    row_index, column_index = result
    print(f'({row_index}, {column_index})')
else:
    print(f'{symbol} does not occur in the matrix')