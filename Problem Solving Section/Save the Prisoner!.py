#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
A jail has a number of prisoners and a number of treats to pass out to them.
Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs.
A chair number will be drawn from a hat.
Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful.
Determine the chair number occupied by the prisoner who will receive that candy.

"""

def saveThePrisoner(n, m, s):
    # Write your code here
    last_sweet = (s + m - 1) % n
    
    if last_sweet:
        return last_sweet
    else:
        return n

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        n = int(first_multiple_input[0])

        m = int(first_multiple_input[1])

        s = int(first_multiple_input[2])

        result = saveThePrisoner(n, m, s)

        fptr.write(str(result) + '\n')

    fptr.close()
