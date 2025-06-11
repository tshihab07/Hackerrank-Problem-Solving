import math
import os
import random
import re
import sys

""" Problem Description:
Given a square matrix, calculate the absolute difference between the sums of its diagonals.

For example, the square matrix arr is shown below:

1 2 3
4 5 6
9 8 9

- The left-to-right diagonal = 1 + 5 + 9 = 16.
- The right-to-left diagonal = 3+ 5 + 6 = 17.
Their absolute difference is | 15 - 17 | = 2.
"""


def diagonalDifference(arr):
    left_sum = 0
    right_sum = 0
    array_size = len(arr)
    n = len(arr)
    for i in range(array_size):
        n -= 1
        for j in range(array_size):
            if i == j:
                left_sum += arr[i][j]
            if n == j:
                right_sum += arr[i][j]
    
    return abs(left_sum - right_sum)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    arr = []

    for _ in range(n):
        arr.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
