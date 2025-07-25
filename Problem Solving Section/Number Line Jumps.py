import math
import os
import random
import re
import sys

""" Problem Description:
You are choreographing a circus show with various animals. For one act, you are given two kangaroos on a number line ready to jump in the positive direction (i.e, toward positive infinity).

The first kangaroo starts at location x1 and moves at a rate of v1 meters per jump.
The second kangaroo starts at location x2 and moves at a rate of v2 meters per jump.
You have to figure out a way to get both kangaroos at the same location at the same time as part of the show. If it is possible, return YES; otherwise, return NO.

Example:
x1 = 2
v1 = 1
x2 = 1
v2 = 2

After one jump, they are both at x = 3. (x1 + v1 = 2 + 1 . x2 + v2 = 1 + 2). So, the answer is Yes

"""

def kangaroo(x1, v1, x2, v2):
    result = "NO"
    if x2 > x1 and v2 > v1:
        return result
    else:
        pos_difference = abs(x2 - x1)
        for i in range(pos_difference):
            x1 += v1
            x2 += v2
            if x1 == x2:
                result = "YES"
                break
    return result
        
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    x1 = int(first_multiple_input[0])

    v1 = int(first_multiple_input[1])

    x2 = int(first_multiple_input[2])

    v2 = int(first_multiple_input[3])

    result = kangaroo(x1, v1, x2, v2)

    fptr.write(result + '\n')

    fptr.close()