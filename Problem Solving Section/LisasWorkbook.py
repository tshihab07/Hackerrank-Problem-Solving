#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
An integer d is a divisor of an integer n if the remainder of n % d = 0.

- There are n chapters in Lisa's workbook, numbered from 1 to n.
- The ith chapter has arr[i] problems, numbered from 1 to arr[i].
- Each page can hold up to k problems. Only a chapter's last page of exercises may contain fewer than k problems.
- Each new chapter starts on a new page, so a page will never contain problems from more than one chapter.
- The page number indexing starts at 1.

Given the details for Lisa's workbook, can you count its number of special problems?
"""


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
