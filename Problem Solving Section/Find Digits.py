#!/bin/python3

import math
import os
import random
import sys

""" Problem Description:
An integer d is a divisor of an integer n if the remainder of n % d = 0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor.
Count the number of divisors occurring within the integer.
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
