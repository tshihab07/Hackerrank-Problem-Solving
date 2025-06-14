#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    time = s.split(":")
    hour = int(time[0])
    minute = int(time[1])
    second = int(time[2][:2])
    
    if 'PM' in time[2]:
        if hour < 12:
            hour += 12
    
    elif 'AM' in time[2]:
        if hour == 12:
            hour = 0
    
    time[0] = hour
    return f"{hour:02d}:{minute:02d}:{second:02d}"
             
            
    # Write your code here

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
