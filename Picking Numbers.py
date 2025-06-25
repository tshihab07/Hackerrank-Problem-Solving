#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'pickingNumbers' function below.
#
# The function is expected to return an INTEGER.
# The function accepts INTEGER_ARRAY a as parameter.
#

def pickingNumbers(a):
    # Write your code here
    freq = [0] * 101

    for num in a:
        freq[num] += 1

    max_len = 0
    for i in range(1, 101):
        # Compare i with (i-1), as their absolute difference is 1
        max_len = max(max_len, freq[i] + freq[i - 1])

    return max_len

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    a = list(map(int, input().rstrip().split()))

    result = pickingNumbers(a)

    fptr.write(str(result) + '\n')

    fptr.close()