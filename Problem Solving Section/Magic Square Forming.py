import math
import os
import random
import re
import sys

""" Problem Description:
We define a magic square to be an n * n  matrix of distinct positive integers from 1 to n^2 
where the sum of any row, column, or diagonal of length  is always equal to the same number: the magic constant. 

You will be given a 3 * 3 matrix of s integers in the inclusive range [1, 9].
We can convert any digit a to b any other digit  in the range [1, 9] at cost of |a-b|.
Given , convert it into a magic square at minimal cost. Print this cost on a new line. 

Note: The resulting magic square must contain distinct integers in the inclusive range [1, 9].
"""

def formingMagicSquare(s):
    # Write your code here
    magic_squares = [
        [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
        [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
        [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
        [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
        [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
        [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
        [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
    ]

    # Compute the minimal cost to convert s into any magic square
    min_cost = float('inf')
    for magic in magic_squares:
        cost = sum(
            abs(s[i][j] - magic[i][j])
            for i in range(3)
            for j in range(3)
        )
        min_cost = min(min_cost, cost)

    return min_cost

    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = []

    for _ in range(3):
        s.append(list(map(int, input().rstrip().split())))

    result = formingMagicSquare(s)

    fptr.write(str(result) + '\n')

    fptr.close()
    sys.stdout.flush()