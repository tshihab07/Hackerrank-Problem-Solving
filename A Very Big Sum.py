#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description: In this challenge, you need to calculate and print the sum of elements in an array, considering that some integers may be very large. """

def aVeryBigSum(ar):
    return sum(ar)
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ar_count = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = aVeryBigSum(ar)

    fptr.write(str(result) + '\n')

    fptr.close()
