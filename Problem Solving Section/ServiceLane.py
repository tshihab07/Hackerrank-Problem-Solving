import math
import os
import random
import re
import sys

""" Problem Description:
A driver is driving on the freeway. The check engine light of his vehicle is on, and the driver wants to get service immediately.
Luckily, a service lane runs parallel to the highway. It varies in width along its length.
We will be given an array of widths at points along the road (indices), then a list of the indices of entry and exit points.
Considering each entry and exit point pair, calculate the maximum size vehicle that can travel that segment of the service lane safely.
"""

def serviceLane(n, cases):
    results = []
    for i, j in cases:
        min_width = min(width[i:j+1])
        results.append(min_width)
    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    width = list(map(int, input().rstrip().split()))

    cases = []

    for _ in range(t):
        cases.append(list(map(int, input().rstrip().split())))

    result = serviceLane(n, cases)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
