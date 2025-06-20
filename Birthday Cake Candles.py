import math
import os
import random
import re
import sys

""" Project Description:
You are in charge of the cake for a child's birthday. It will have one candle for each year of their total age.
They will only be able to blow out the tallest of the candles. Your task is to count how many candles are the tallest.
Example:
candles = [4, 4, 1, 3]
The tallest candles are 4 units high. There are 2 candles with this height, so the function should return 2.
"""

def birthdayCakeCandles(candles):
    tall_candle = max(candles)
    return candles.count(tall_candle)

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    candles_count = int(input().strip())

    candles = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(candles)

    fptr.write(str(result) + '\n')

    fptr.close()
