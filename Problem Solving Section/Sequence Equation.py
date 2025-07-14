#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'permutationEquation' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY p as parameter.
#

def permutationEquation(p):

    result = []
    # Create a value-to-index map for fast lookup
    index_map = {value: idx + 1 for idx, value in enumerate(p)}

    for x in range(1, len(p) + 1):
        y = index_map[index_map[x]]
        result.append(y)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
