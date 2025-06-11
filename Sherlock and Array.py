import math
import os
import random
import re
import sys

""" Problem Description:
Watson gives Sherlock an array of integers.
His challenge is to find an element of the array such that the sum of all elements to the left is equal to the sum of all elements to the right.

Example -
arr = [5, 6, 8, 11]
8 is between two subarrays that sum to 11.
arr[1]
the ans is [1] since left and right sum is 0.
You will be given arrays of integers and must determine whether there is an element that meets the criterion.
If there is, return YES. Otherwise, return NO.

"""

def balancedSums(arr):
    # Write your code here
    left_sum = 0
    arr_sum = sum(arr)
    
    for i in arr:
        
        if (2 * left_sum) == arr_sum - i:
            return "YES"
        
        left_sum += i
        
    return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    T = int(input().strip())

    for T_itr in range(T):
        n = int(input().strip())

        arr = list(map(int, input().rstrip().split()))

        result = balancedSums(arr)

        fptr.write(result + '\n')

    fptr.close()
