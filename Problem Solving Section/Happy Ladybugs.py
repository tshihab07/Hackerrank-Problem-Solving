#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'happyLadybugs' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING b as parameter.
#

def happyLadybugs(b):
    
    n = len(b)
    # Count frequencies
    freq = {}
    for ch in b:
        freq[ch] = freq.get(ch, 0) + 1
    
    # Any color (not '_') with count 1 → impossible
    for ch in freq:
        if ch != '_' and freq[ch] == 1:
            return "NO"
    
    # If there's at least one '_', we can rearrange → YES
    if '_' in freq:
        return "YES"
    
    # No empty cells: check if already happy
    for i in range(n):
        if b[i] == '_':
            continue
        left = (i > 0 and b[i-1] == b[i])
        right = (i < n-1 and b[i+1] == b[i])
        
        if not (left or right):
            return "NO"
    
    return "YES"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    g = int(input().strip())

    for g_itr in range(g):
        n = int(input().strip())

        b = input()

        result = happyLadybugs(b)

        fptr.write(result + '\n')

    fptr.close()
