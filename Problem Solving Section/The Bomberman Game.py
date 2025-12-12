#!/bin/python3

import math
import os
import random
import re
import sys

""" Description: Bomberman lives in a rectangular grid. Each cell in the grid either contains a bomb or nothing at all.

Each bomb can be planted in any cell of the grid but once planted, it will detonate after exactly 3 seconds
 Once a bomb detonates, it's destroyed — along with anything in its four neighboring cells.
 This means that if a bomb detonates in cell i, j, any valid cells (i +/- 1, j) and (1, j +/- 1) are cleared.
 If there is a bomb in a neighboring cell, the neighboring bomb is destroyed without detonating, so there's no chain reaction.

Bomberman is immune to bombs, so he can move freely throughout the grid. Here's what he does:

- Initially, Bomberman arbitrarily plants bombs in some of the cells, the initial state.
- After one second, Bomberman does nothing.
- After one more second, Bomberman plants bombs in all cells without bombs, thus filling the whole grid with bombs.
No bombs detonate at this point.
- After one more second, any bombs planted exactly three seconds ago will detonate. Here, Bomberman stands back and observes.
- Bomberman then repeats steps 3 and 4 indefinitely.
Note that during every second Bomberman plants bombs, the bombs are planted simultaneously (i.e., at the exact same moment),
and any bombs planted at the same time will detonate at the same time.

Given the initial configuration of the grid with the locations of Bomberman's first batch of planted bombs,
determine the state of the grid after N seconds.
"""

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
