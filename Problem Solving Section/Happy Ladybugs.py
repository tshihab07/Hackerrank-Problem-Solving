#!/bin/python3

import math
import os
import random
import re
import sys

"""Description: Happy Ladybugs is a board game having the following properties:

- The board is represented by a string, b, of length n. The i-th character of the string, b[i], denotes the i-th cell of the board.
- If b[i] is an underscore (i.e., _), it means the i-th cell of the board is empty.
- If b[i] is an uppercase English alphabetic letter (ascii[A-Z]), it means the i-th cell contains a ladybug of color b[i].
- String b will not contain any other characters.
- A ladybug is happy only when its left or right adjacent cell (i.e., b[i+/-1) is occupied by another ladybug having the same color.
- In a single move, you can move a ladybug from its current position to any empty cell.
Given the values of n and b for g games of Happy Ladybugs, determine if it's possible to make all the ladybugs happy.
For each game, return YES if all the ladybugs can be made happy through some number of moves. Otherwise, return NO.
"""

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
