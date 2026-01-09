import math
import os
import random
import re
import sys

""" Description: Given an array of strings of digits, try to find the occurrence of a given pattern of digits.
In the grid and pattern arrays, each string represents a row in the grid. For example, consider the following grid:
1234567890  
0987654321  
1111111111  
1111111111  
2222222222  
The pattern array is:

876543  
111111  
111111
The pattern begins at the second row and the third column of the grid and continues in the following two rows.
The pattern is said to be present in the grid. The return value should be YES or NO, depending on whether the pattern is found.
In this case, return YES.
"""

def gridSearch(G, P):
    R = len(G)
    C = len(G[0])
    r = len(P)
    c = len(P[0])
    
    # iterate over all possible top-left positions
    for i in range(R - r + 1):
        for j in range(C - c + 1):
            # check if pattern matches starting at (i, j)
            match = True
            
            for di in range(r):
                if G[i + di][j:j + c] != P[di]:
                    match = False
                    break
            
            if match:
                return "YES"
    
    return "NO"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        R = int(first_multiple_input[0])

        C = int(first_multiple_input[1])

        G = []

        for _ in range(R):
            G_item = input()
            G.append(G_item)

        second_multiple_input = input().rstrip().split()

        r = int(second_multiple_input[0])

        c = int(second_multiple_input[1])

        P = []

        for _ in range(r):
            P_item = input()
            P.append(P_item)

        result = gridSearch(G, P)

        fptr.write(result + '\n')

    fptr.close()
