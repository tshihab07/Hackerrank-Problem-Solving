import math
import os
import random
import re
import sys
import itertools

""" Problem Description:
Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers.
Then print the respective minimum and maximum values as a single line of two space-separated long integers.
Example:
arr = [1, 3, 5, 7, 9]
The minimum sum is 1+ 3 + 5 + 7 = 16, and the maximum sum is 3 + 5 + 7 + 9 = 24. The function prints 16 24
"""


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
