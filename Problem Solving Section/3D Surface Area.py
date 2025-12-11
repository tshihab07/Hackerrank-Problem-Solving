#!/bin/python3

import math
import os
import random
import re
import sys


""" Description: Madison is a little girl who is fond of toys.
Her friend Mason works in a toy manufacturing factory .
Mason has a 2D board A of size H x W with H rows and W columns.
The board is divided into cells of size 1 x 1 with each cell indicated by its coordinate (i, j).
The cell (i, j) has an integer A[i, j] written on it. To create the toy Mason stacks A[i, j] number of cubes of size 1 x 1 x on the cell (i, j).

Given the description of the board showing the values of A[i, j]
and that the price of the toy is equal to the 3d surface area find the price of the toy."""


def surfaceArea(A):
    H = len(A)
    W = len(A[0])
    total = 0
    
    for i in range(H):
        for j in range(W):
            h = A[i][j]
            
            if h == 0:
                continue
            
            total += 2
            up = A[i-1][j] if i > 0 else 0
            down = A[i+1][j] if i < H-1 else 0
            left = A[i][j-1] if j > 0 else 0
            right = A[i][j+1] if j < W-1 else 0
            total += max(0, h - up)
            total += max(0, h - down)
            total += max(0, h - left)
            total += max(0, h - right)
    
    return total


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    H = int(first_multiple_input[0])

    W = int(first_multiple_input[1])

    A = []

    for _ in range(H):
        A.append(list(map(int, input().rstrip().split())))

    result = surfaceArea(A)

    fptr.write(str(result) + '\n')

    fptr.close()
