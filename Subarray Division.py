import math
import os
import random
import re
import sys

""" Problem Description:
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.

Lily decides to share a contiguous segment of the bar selected such that:

- The length of the segment matches Ron's birth month, and,
- The sum of the integers on the squares is equal to his birth day.
Determine how many ways she can divide the chocolate.

Example- 
s = [2, 2, 1, 3, 2]
d = 4
m = 2

Lily wants to find segments summing to Ron's birth day, d = 4 with a length equalling his birth month, m = 2.
In this case, there are two segments meeting her criteria: [2, 2] and [3, 1]
"""

def birthday(s, d, m):
    # Write your code here
    count = 0

    for i in range(len(s) - m + 1):
        if sum(s[i:i + m]) == d:
            count += 1

    return count

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    s = list(map(int, input().rstrip().split()))

    first_multiple_input = input().rstrip().split()

    d = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    result = birthday(s, d, m)

    fptr.write(str(result) + '\n')

    fptr.close()
