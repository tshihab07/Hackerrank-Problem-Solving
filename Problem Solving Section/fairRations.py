#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'fairRations' function below.
#
# The function is expected to return a STRING.
# The function accepts INTEGER_ARRAY B as parameter.
#

def fairRations(B):
    # Count odd numbers
    odd_count = sum(1 for x in B if x % 2 == 1)
    if odd_count % 2 != 0:
        return "NO"
    
    loaves = 0
    # Make a copy
    B = B[:]
    
    for i in range(len(B) - 1):  # stop at second last
        if B[i] % 2 == 1:
            # Give 1 loaf to i and i+1
            B[i] += 1
            B[i + 1] += 1
            loaves += 2
    
    return loaves


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    N = int(input().strip())

    B = list(map(int, input().rstrip().split()))

    result = fairRations(B)

    fptr.write(result + '\n')

    fptr.close()
