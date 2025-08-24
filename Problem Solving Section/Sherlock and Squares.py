#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
Watson likes to challenge Sherlock's math ability.
He will provide a starting and ending value that describe a range of integers, inclusive of the endpoints.
Sherlock must determine the number of square integers within that range.
Example:
a = 24
b = 49
The square integers in this range are 25, 36, and 49. Return 3.
"""

def squares(a, b):
    smallest_perfect_square = math.ceil(math.sqrt(a))
    largest_perfect_square = math.floor(math.sqrt(b))
    total_perfect_square = largest_perfect_square - smallest_perfect_square + 1
    
    return  total_perfect_square


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        first_multiple_input = input().rstrip().split()

        a = int(first_multiple_input[0])

        b = int(first_multiple_input[1])

        result = squares(a, b)

        fptr.write(str(result) + '\n')

    fptr.close()