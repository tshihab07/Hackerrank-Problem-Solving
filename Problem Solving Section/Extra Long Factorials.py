#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description: 
The factorial of the integer n, written n!, is defined as:

n! = n * (n - 1) * (n - 2) * .... * 3 * 2 * 1


Calculate and print the factorial of a given integer.

For example, if n = 30, we calculate


30 * 29 * 28 * ..... * 2 * 1


and get
265252859812191058636308480000000.

"""

def extraLongFactorials(n):
    # Write your code here
    fact = 1
    for i in range(2, n+1):
        fact *= i
    
    print(fact)

if __name__ == '__main__':
    n = int(input().strip())

    extraLongFactorials(n)