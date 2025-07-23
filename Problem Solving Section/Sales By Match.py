import math
import os
import random
import re
import sys

""" Problem Description:
There is a large pile of socks that must be paired by color.
Given an array of integers representing the color of each sock, determine how many pairs of socks with matching colors there are.
Example:
n = 7
ar = [1, 2, 1, 2, 1, 3, 2]
There is one pair of color 1 and one of color 2. There are three odd socks left, one of each color. The number of pairs is 2.
"""

def sockMerchant(n, ar):
    # Write your code here
    sock_color = {}
    for sock in ar:
        sock_color[sock] = sock_color.get(sock, 0) + 1
    
    pair_count = 0
    for count in sock_color.values():
        pair_count += (count // 2)
    
    
    return pair_count
    
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    ar = list(map(int, input().rstrip().split()))

    result = sockMerchant(n, ar)

    fptr.write(str(result) + '\n')

    fptr.close()
