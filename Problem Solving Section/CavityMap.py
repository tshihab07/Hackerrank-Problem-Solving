#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'cavityMap' function below.
#
# The function is expected to return a STRING_ARRAY.
# The function accepts STRING_ARRAY grid as parameter.
#

def cavityMap(grid):
    n = len(grid)
    # If grid is too small (n <= 2), no interior cells → return as is
    if n <= 2:
        return grid
    
    # Convert each row to list of chars for mutation
    grid = [list(row) for row in grid]
    
    for i in range(1, n - 1):
        for j in range(1, n - 1):
            current = grid[i][j]
            # Check 4 neighbors: up, down, left, right
            if (current > grid[i-1][j] and
                current > grid[i+1][j] and
                current > grid[i][j-1] and
                current > grid[i][j+1]):
                grid[i][j] = 'X'
    
    # Convert back to list of strings
    return [''.join(row) for row in grid]

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    grid = []

    for _ in range(n):
        grid_item = input()
        grid.append(grid_item)

    result = cavityMap(grid)

    fptr.write('\n'.join(result))
    fptr.write('\n')

    fptr.close()
