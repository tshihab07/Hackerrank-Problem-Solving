#!/bin/python3

import math
import os
import random
import re
import sys

""" Description: We define P to be a permutation of the first n natural numbers in the range [1, n].
Let pos[i] denote the value at position i in permutation P using 1-based indexing.

P is considered to be an absolute permutation if |pos[i] - i| = k holds true for every i ε [1, n].

Given n and k, print the lexicographically smallest absolute permutation P. If no absolute permutation exists, print -1.
"""



def absolutePermutation(n, k):
    if k == 0:
        return list(range(1, n+1))
    
    if n % (2 * k) != 0:
        return [-1]
    
    res = [0] * n
    
    for start in range(0, n, 2 * k):
        for i in range(start, start + k):
            # First half of block: assign i+1+k
            res[i] = i + 1 + k
            # Second half: assign i+1
            res[i + k] = i + 1
    
    return res


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        k = int(first_multiple_input[1])

        result = absolutePermutation(n, k)

        fptr.write(' '.join(map(str, result)))
        fptr.write('\n')

    fptr.close()
