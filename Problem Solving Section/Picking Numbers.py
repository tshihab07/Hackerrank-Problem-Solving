#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
Example:
a = [1, 1, 2, 2, 4, 4, 5, 5, 5]
There are two subarrays meeting the criterion: [1, 1, 2, 2] and [4, 4, 5, 5, 5]. The maximum length subarray has 5 elements.
"""

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