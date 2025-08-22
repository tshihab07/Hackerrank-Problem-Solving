#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
There is a string, s, of lowercase English letters that is repeated infinitely many times.
Given an integer, n, find and print the number of letter a's in the first n letters of the infinite string.

Example:
s = 'abcac'
n = 10
The substring we consider is 'abcacabcac', which contains 4 occurrences of 'a'.
The function should return 4.
"""

def repeatedString(s, n):
    count_a_in_s = s.count('a')
    full_repeats = n // len(s)
    remainder = n % len(s)
    total_count = count_a_in_s * full_repeats + s[:remainder].count('a')
    
    return total_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    n = int(input().strip())

    result = repeatedString(s, n)

    fptr.write(str(result) + '\n')

    fptr.close()
