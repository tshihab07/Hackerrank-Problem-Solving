import math
import os
import random
import re
import sys


def beautifulTriplets(d, arr):
    s = set(arr)  # for O(1) lookups
    count = 0
    for x in arr:
        if (x + d in s) and (x + 2*d in s):
            count += 1
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = beautifulTriplets(d, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
