import sys
from io import StringIO

test_input1 = '''3, 6
7 1 3 3 2 1
1 3 9 8 5 6
4 6 7 9 1 0
'''
test_input2 = '''3
1, 2, 3
4, 5, 6
7, 8, 9
'''

# sys.stdin = StringIO(test_input1)
# sys.stdin = StringIO(test_input2)

n = int(input())
matrix = []
for _ in range(n):
    matrix.append(
        [int(x) for x in input().split()]
    )
primary = []
secondary = []
for indx in range(n):
    primary.append(matrix[indx][indx])
    secondary.append(matrix[indx][n - 1 - indx])
primary_sum = sum(primary)
secondary_sum = sum(secondary)
print(abs(primary_sum - secondary_sum))