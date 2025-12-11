#!/bin/python3

import math
import os
import random
import re
import sys

""" Description: There is a strange counter.
At the first second, it displays the number 3. Each second, the number displayed by decrements by 1 until it reaches 1.
In next second, the timer resets to 2 x the initial number for the prior cycle and continues counting down.
The diagram below shows the counter values for each time  in the first three cycles:


"""

def strangeCounter(t):
    start_time = 1
    value = 3
    while t >= start_time + value:
        start_time += value
        value *= 2
    return value - (t - start_time)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    result = strangeCounter(t)

    fptr.write(str(result) + '\n')

    fptr.close()
