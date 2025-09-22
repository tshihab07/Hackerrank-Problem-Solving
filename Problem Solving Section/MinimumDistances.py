#!/bin/python3

import math
import os
import random
import re
import sys


def minimumDistances(a):
    # Write your code here
    last_seen = {}
    min_dist = float('inf')
    
    for i, num in enumerate(a):
        if num in last_seen:
            dist = i - last_seen[num]
            min_dist = min(min_dist, dist)
        last_seen[num] = i  # update last seen index
    
    return min_dist if min_dist != float('inf') else -1


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = minimumDistances(a)

    fptr.write(str(result) + '\n')

    fptr.close()