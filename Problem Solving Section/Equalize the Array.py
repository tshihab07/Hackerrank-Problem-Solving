#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

""" Problem Description: Given an array of integers,
determine the minimum number of elements to delete to leave only elements of equal value.
Example:
arr =  [1, 2, 2, 3]

Delete the 2 elements 1 and 3 leaving [2, 2].
If both twos plus either the 1 or the 3 are deleted, it takes 2 deletions to leave either 1 or 3. The minimum number of deletions is 2.
"""


def equalizeArray(arr):
    # Write your code here
    freq = Counter(arr)             # Count each number's occurrences
    max_freq = max(freq.values())   # Most frequent number count
    return len(arr) - max_freq      # Remove everything else


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = equalizeArray(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
