#!/bin/python3

import math
import os
import random
import re
import sys


def fairRations(B):
    odd_count = 0
    
    for x in B:
        if x % 2 == 1:
            odd_count += 1
    
    if odd_count % 2 == 1:
        return "NO"
    
    loaves = 0
    
    for i in range(len(B) - 1):
        if B[i] % 2 == 1:
            B[i] += 1
            B[i + 1] += 1
            loaves += 2
    
    return str(loaves)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')
    
    N = int(input().strip())
    
    B = list(map(int, input().rstrip().split()))
    
    result = fairRations(B)
    
    fptr.write(result + '\n')
    
    fptr.close()