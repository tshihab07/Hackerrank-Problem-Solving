import math
import os
import random
import sys

""" Problem Description:
HackerLand Enterprise is adopting a new viral advertising strategy.
When they launch a new product, they advertise it to exactly 5 people on social media.
Each person shares the advertisement with 3 of their friends on the next day. The process continues for a total of n days.

The task is to determine the total number of likes the advertisement will receive after n days.
"""

def viralAdvertising(n):
    shared = 5
    total_likes = 0

    for day in range(n):
        likes = shared // 2
        total_likes += likes
        shared = likes * 3 

    return total_likes

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    result = viralAdvertising(n)

    fptr.write(str(result) + '\n')

    fptr.close()