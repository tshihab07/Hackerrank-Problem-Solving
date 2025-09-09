""" Problem Description:
David has several containers, each with a number of balls in it.
He has just enough containers to sort each type of ball he has into its own container.
David wants to sort the balls using his sort method. David wants to perform some number of swap operations such that: Each container contains only balls of the same type.
No two balls of the same type are located in different containers.
"""

#!/bin/python3

import math
import os
import random
import re
import sys

def organizingContainers(container):
    # Total balls in each container
    container_sums = [sum(row) for row in container]
    
    # Total balls of each type
    type_sums = [sum(col) for col in zip(*container)]
    
    # Check if the multisets match
    if sorted(container_sums) == sorted(type_sums):
        return "Possible"
    else:
        return "Impossible"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input().strip())

    for q_itr in range(q):
        n = int(input().strip())

        container = []

        for _ in range(n):
            container.append(list(map(int, input().rstrip().split())))

        result = organizingContainers(container)

        fptr.write(result + '\n')

    fptr.close()

