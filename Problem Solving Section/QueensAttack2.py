#!/bin/python3

import math
import os
import random
import re
import sys


def queensAttack(n, k, r_q, c_q, obstacles):
    obstacles = set(map(tuple, obstacles))
    
    moves = [
        (1, 0), (-1, 0),   # up, down
        (0, 1), (0, -1),   # right, left
        (1, 1), (1, -1),   # up-right, up-left
        (-1, 1), (-1, -1)  # down-right, down-left
    ]
    
    count = 0
    for dr, dc in moves:
        r, c = r_q + dr, c_q + dc
        while 1 <= r <= n and 1 <= c <= n and (r, c) not in obstacles:
            count += 1
            r += dr
            c += dc
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    r_q = int(second_multiple_input[0])

    c_q = int(second_multiple_input[1])

    obstacles = []

    for _ in range(k):
        obstacles.append(list(map(int, input().rstrip().split())))

    result = queensAttack(n, k, r_q, c_q, obstacles)

    fptr.write(str(result) + '\n')

    fptr.close()
