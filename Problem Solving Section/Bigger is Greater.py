import math
import os
import random
import re
import sys

""" Problem Description:
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.
Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:
- It must be greater than the original word
- It must be the smallest word that meets the first condition.
"""


def biggerIsGreater(w):
    # Convert string to list for easy manipulation
    w = list(w)
    n = len(w)
    
    # Find the first decreasing element from the right
    i = n - 2
    while i >= 0 and w[i] >= w[i + 1]:
        i -= 1
    
    if i == -1:  # Entire string is non-increasing
        return "no answer"
    
    # Find the smallest character on right side that is larger than w[i]
    j = n - 1
    while w[j] <= w[i]:
        j -= 1
    
    # Swap
    w[i], w[j] = w[j], w[i]
    
    # Reverse the suffix
    w[i+1:] = reversed(w[i+1:])
    
    return ''.join(w)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)

        fptr.write(result + '\n')

    fptr.close()

