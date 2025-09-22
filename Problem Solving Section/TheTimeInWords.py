#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeInWords' function below.
#
# The function is expected to return a STRING.
# The function accepts following parameters:
#  1. INTEGER h
#  2. INTEGER m
#

def timeInWords(h, m):
    # Write your code here
    # Map numbers to words (0 to 29 is enough)
    nums = [
        "zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine",
        "ten", "eleven", "twelve", "thirteen", "fourteen", "fifteen", "sixteen",
        "seventeen", "eighteen", "nineteen", "twenty", "twenty one", "twenty two",
        "twenty three", "twenty four", "twenty five", "twenty six", "twenty seven",
        "twenty eight", "twenty nine"
    ]
    
    if m == 0:
        return f"{nums[h]} o' clock"
    elif m == 1:
        return f"one minute past {nums[h]}"
    elif m == 15:
        return f"quarter past {nums[h]}"
    elif m == 30:
        return f"half past {nums[h]}"
    elif m == 45:
        next_hour = nums[h + 1] if h < 12 else "one"
        return f"quarter to {next_hour}"
    elif m < 30:
        return f"{nums[m]} minutes past {nums[h]}"
    else:  # m > 30 and m != 45
        remaining = 60 - m
        next_hour = nums[h + 1] if h < 12 else "one"
        if remaining == 1:
            return f"one minute to {next_hour}"
        else:
            return f"{nums[remaining]} minutes to {next_hour}"


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = int(input().strip())

    m = int(input().strip())

    result = timeInWords(h, m)

    fptr.write(result + '\n')

    fptr.close()
