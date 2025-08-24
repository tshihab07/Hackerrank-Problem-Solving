import math
import os
import random
import re
import sys

""" Project Description:
Given a time in 12-hour AM/PM format, convert it to military (24-hour) time.
Note: - 12:00:00AM on a 12-hour clock is 00:00:00 on a 24-hour clock.
- 12:00:00PM on a 12-hour clock is 12:00:00 on a 24-hour clock.

Example
s = '12:01:00 PM'

Return '12:01:00'.

s = '12:01:00 AM'
Return '00:01:00'.
"""

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
             

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()