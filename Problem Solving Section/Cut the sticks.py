import math
import os
import random
import re
import sys

""" Problem Description:
You are given a number of sticks of varying lengths.
You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left.
At each iteration you will determine the length of the shortest stick remaining,
cut that length from each of the longer sticks and then discard all the pieces of that shortest length.
When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of n sticks, print the number of sticks that are left before each iteration until there are none left.
Example:
arr = [1, 2, 3]
The shortest stick length is 1, so we cut all sticks by 1.
"""

def cutTheSticks(arr):
    result = []
    
    while arr:
        result.append(len(arr))
        min_val = min(arr)
        arr = [x - min_val for x in arr if x - min_val > 0]
        
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()