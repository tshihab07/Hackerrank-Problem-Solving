#!/bin/python3

import math
import os
import random
import re
import sys


def workbook(n, k, arr):
    page = 1
    special = 0
    for problems in arr:
        start = 1
        while start <= problems:
            end = min(start + k - 1, problems)
            if start <= page <= end:
                special += 1
            page += 1
            start = end + 1
    return special


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    result = workbook(n, k, arr)

    fptr.write(str(result) + '\n')

    fptr.close()
