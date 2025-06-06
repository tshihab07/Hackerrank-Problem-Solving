#!/bin/python3

import math
import os
import random
import re
import sys
import itertools
#
# Complete the 'miniMaxSum' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def miniMaxSum(arr):
    arr_tuple = list(itertools.combinations(arr, 4))
    min_sum = sum(arr_tuple[0])
    max_sum = sum(arr_tuple[0])
    
    for sl in arr_tuple:
        total_sum = sum(sl)
        if min_sum > total_sum:
            min_sum = total_sum
        if max_sum < total_sum:
            max_sum = total_sum
    
    return min_sum, max_sum
    # Write your code here

if __name__ == '__main__':

    arr = list(map(int, input().rstrip().split()))

    mn_sum, mx_sum = miniMaxSum(arr)
    print(mn_sum, mx_sum)
