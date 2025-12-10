#!/bin/python3

import math
import os
import random
import re
import sys

""" Description: Manasa is out on a hike with friends. She finds a trail of stones with numbers on them.
She starts following the trail and notices that any two consecutive stones' numbers differ by one of two values.
Legend has it that there is a treasure trove at the end of the trail.
If Manasa can guess the value of the last stone, the treasure will be hers.
"""
def stones(n, a, b):
    # Number of steps = n - 1
    steps = n - 1
    values = set()
    for i in range(steps + 1):
        # i times a, (steps - i) times b
        val = i * a + (steps - i) * b
        values.add(val)
    return sorted(values)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        a = int(input().strip())

        b = int(input().strip())

        result = stones(n, a, b)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()