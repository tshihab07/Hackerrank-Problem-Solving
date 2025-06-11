import math
import os
import random
import re
import sys

""" Problem Description:
Its base and height are both equal to n. It is drawn using # symbols and spaces. The last line is not preceded by any spaces.

Write a program that prints a staircase of size n.
"""

def staircase(n):
    for i in range(n):
        for j in range(n-i-1):
            print(" ", end="")
        for j in range(i+1):
            print("#", end="")
        
        print()
    # Write your code here

if __name__ == '__main__':
    n = int(input().strip())

    staircase(n)
