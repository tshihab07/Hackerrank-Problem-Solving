#!/bin/python3

import math
import os
import random
import re
import sys


def kaprekarNumbers(p, q):
    # Write your code here
    kaprekars = []
    for n in range(p, q + 1):
        sq = n * n
        sq_str = str(sq)
        d = len(str(n))
        
        # Split into left and right parts
        # Right part must be d digits
        r_str = sq_str[-d:]  # last d digits
        l_str = sq_str[:-d]  # everything else (could be empty)
        
        # Handle case where l_str is empty
        l = int(l_str) if l_str != '' else 0
        r = int(r_str)
        
        if l + r == n:
            kaprekars.append(n)
    
    if kaprekars:
        print(" ".join(map(str, kaprekars)))
    else:
        print("INVALID RANGE")


if __name__ == '__main__':
    p = int(input().strip())

    q = int(input().strip())

    kaprekarNumbers(p, q)
