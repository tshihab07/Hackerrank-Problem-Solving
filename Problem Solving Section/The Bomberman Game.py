

#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'bomberMan' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts following parameters:
#  1. INTEGER n
#  2. STRING_ARRAY grid
#

def bomberMan(n, grid):
    r = len(grid)
    c = len(grid[0])
    # mark destroyed cells
    destroy = [[False]*c for _ in range(r)]
    dirs = [(0,1),(0,-1),(1,0),(-1,0)]
    for i in range(r):
        for j in range(c):
            if grid[i][j] == 'O':
                destroy[i][j] = True
                for di, dj in dirs:
                    ni, nj = i+di, j+dj
                    if 0 <= ni < r and 0 <= nj < c:
                        destroy[ni][nj] = True
    # Build result
    res = []
    for i in range(r):
        row = ''.join('.' if destroy[i][j] else 'O' for j in range(c))
        res.append(row)
    return res

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    r = int(first_multiple_input[0])

    c = int(first_multiple_input[1])

    n = int(first_multiple_input[2])

    grid = []

    for _ in range(r):
        grid_item = input()
        grid.append(grid_item)

    result = bomberMan(n, grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
