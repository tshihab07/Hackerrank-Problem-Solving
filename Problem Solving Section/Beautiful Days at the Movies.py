#!/bin/python3

import os

""" Problem Description:
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse.
For instance, given the number 12,  its reverse is 21. Their difference is 9.
The number 120 reversed is 21, and their difference is 99.
She decides to apply her game to decision making.
She will look at a numbered range of days and will only go to a movie on a beautiful day.

Given a range of numbered days, [i...j] and a number k, determine the number of days in the range that are beautiful.
Beautiful numbers are defined as numbers where |i - reversed(i)| is evenly divisible by k.
If a day's value is a beautiful number, it is a beautiful day.
Return the number of beautiful days in the range.
"""

def beautifulDays(i, j, k):
    # Write your code here
    day_count = 0
    for day in range(i, j+1):
        if abs(day - int(str(day)[::-1])) % k == 0:
            day_count += 1
    
    return day_count


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    i = int(first_multiple_input[0])

    j = int(first_multiple_input[1])

    k = int(first_multiple_input[2])

    result = beautifulDays(i, j, k)

    fptr.write(str(result) + '\n')

    fptr.close()
