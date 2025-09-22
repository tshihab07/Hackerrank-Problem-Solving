#!/bin/python3

import math
import os
import random
import re
import sys


def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    if p > s:
        return 0
    
    # Phase 1: Buy games while price is above m
    games = 0
    current = p
    total = 0

    # While price is above m and we can afford next game
    while current > m and total + current <= s:
        total += current
        games += 1
        current -= d

    # Phase 2: All remaining games cost m
    if total < s:
        remaining_money = s - total
        games += remaining_money // m

    return games


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
