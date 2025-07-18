import math
import os
import random
import re
import sys

""" Problem Description:
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:

- The elements of the first array are all factors of the integer being considered
- The integer being considered is a factor of all elements of the second array.
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.

Example - 
a = [2, 6]
b = [24, 36]

There are two numbers between the arrays: 6 and 12.
6%2 = 0. 6%6 = 0. 24%6 = 0. 36%6 = 0 for the first value.
12%2 = 0. 12%6 = 0. 24%2 = 0. 36%12 = 0 for the second value.

Return 2.

"""

def getTotalX(a, b):
    # Write your code here
    list2_lowest = min(b)
    
    count = 0
    
    for i in range(min(a), list2_lowest+1):
        for j in a:
            if i % j == 0:
                flag = True
            else:
                flag = False
                break
            
        if flag == True:
            for k in b:
                if k % i == 0:
                    flag2 = True
                else:
                    flag2 = False
                    break
                    
            if flag2 == True:
                count += 1
    
    return count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    m = int(first_multiple_input[1])

    arr = list(map(int, input().rstrip().split()))

    brr = list(map(int, input().rstrip().split()))

    total = getTotalX(arr, brr)

    fptr.write(str(total) + '\n')

    fptr.close()
