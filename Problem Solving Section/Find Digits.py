#!/bin/python3

import math
import os
import random
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

def findDigits(n):
    # Write your code here
    count = 0
    for num in str(n):
        try:
            if n % int(num) == 0:
                count += 1
        
        except ZeroDivisionError:
            pass
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        n = int(input().strip())

        result = findDigits(n)

        fptr.write(str(result) + '\n')

    fptr.close()
