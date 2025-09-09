""" Problem Description:
An English text needs to be encrypted using the following encryption scheme.
First, the spaces are removed from the text. Let L be the length of this text.
"""
#!/bin/python3

import math
import os
import random
import re
import sys


def encryption(s):
    # remove spaces
    s = s.replace(" ", "")
    L = len(s)
    
    # determine rows and columns
    rows = math.floor(math.sqrt(L))
    cols = math.ceil(math.sqrt(L))
    
    if rows * cols < L:
        rows += 1
    
    # build the encrypted message
    encrypted = []
    for c in range(cols):
        word = ''.join(s[i] for i in range(c, L, cols))
        encrypted.append(word)
    
    return ' '.join(encrypted)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = encryption(s)

    fptr.write(result + '\n')

    fptr.close()

