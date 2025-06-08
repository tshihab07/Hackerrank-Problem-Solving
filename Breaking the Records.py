#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'breakingRecords' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts INTEGER_ARRAY scores as parameter.
#

def breakingRecords(scores):

    highest_score = scores[0]
    lowest_score = scores[0]
    new_record_count = 0
    worst_record_count = 0

    for score in scores[1:]:
        if score > highest_score:
            highest_score = score
            new_record_count += 1
        elif score < lowest_score:
            lowest_score = score
            worst_record_count += 1

    return [new_record_count, worst_record_count]
            
            
        
        

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    scores = list(map(int, input().rstrip().split()))

    result = breakingRecords(scores)

    fptr.write(' '.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
