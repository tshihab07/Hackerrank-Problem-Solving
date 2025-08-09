#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description: There is a new mobile game that starts with consecutively numbered clouds.
Some of the clouds are thunderheads and others are cumulus.
The player can jump on any cumulus cloud having a number that is equal to the number of the current cloud plus 1 or 2.
The player must avoid the thunderheads. Determine the minimum number of jumps it will take to jump from the
starting postion to the last cloud. It is always possible to win the game.

For each game, you will get an array of clouds numbered 0 if they are safe or 1 if they must be avoided."""

def jumpingOnClouds(c):
    jumps = 0
    position = 0
    n = len(c)

    while position < n - 1:
        # Try to jump 2 steps if possible and safe
        if position + 2 < n and c[position + 2] == 0:
            position += 2
        else:
            position += 1
        jumps += 1

    return jumps

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c)

    fptr.write(str(result) + '\n')

    fptr.close()
