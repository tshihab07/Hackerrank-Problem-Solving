#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
Little Bobby loves chocolate. He frequently goes to his favorite 5 & 10 store, Penny Auntie, to buy them.
They are having a promotion at Penny Auntie. If Bobby saves enough wrappers, he can turn them in for a free chocolate.
"""


def chocolateFeast(n, c, m):
    # Write your code here
    chocolates = n // c  # initial chocolates
    wrappers = chocolates
    
    while wrappers >= m:
        free = wrappers // m
        chocolates += free
        wrappers = wrappers % m + free  # leftover + new wrappers from free chocolates
    
    return chocolates


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        c = int(first_multiple_input[1])

        m = int(first_multiple_input[2])

        result = chocolateFeast(n, c, m)

        fptr.write(str(result) + '\n')

    fptr.close()
