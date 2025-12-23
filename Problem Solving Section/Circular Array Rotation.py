import math
import os
import random
import re
import sys

""" Problem Description:
John Watson knows of an operation called a right circular rotation on an array of integers.
One rotation operation moves the last array element to the first position and shifts all remaining elements right one.
To test Sherlock's abilities, Watson provides Sherlock with an array of integers.
Sherlock is to perform the rotation operation a number of times then determine the value of the element at a given position.

For each array, perform a number of right circular rotations and return the values of the elements at the given indices.
"""


def circularArrayRotation(a, k, queries):
    # Write your code here
    n = len(a)
    k = k % n
    rotated = a[-k:] + a[:-k]

    return [rotated[q] for q in queries]


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    q = int(first_multiple_input[2])

    a = list(map(int, input().rstrip().split()))

    queries = []

    for _ in range(q):
        queries_item = int(input().strip())
        queries.append(queries_item)

    result = circularArrayRotation(a, k, queries)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
