#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter


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
