""" Problem Description:
# Count Elements Greater Than Previous Average
Given an array of positive integers,
return the number of elements that are strictly greater than the average of all previous elements.
Skip the first element."""

import math
import os
import random
import re
import sys


def countResponseTimeRegressions(responseTimes):
    if not responseTimes:
        return 0
    
    count = 0
    running_sum = 0
    
    for i in range(1, len(responseTimes)):
        running_sum += responseTimes[i - 1]             # sum of elements before index i
        previous_avg = running_sum / i                  # average of first i elements (indices 0 to i-1)
        if responseTimes[i] > previous_avg:
            count += 1
            
    return count

if __name__ == '__main__':
    responseTimes_count = int(input().strip())

    responseTimes = []

    for _ in range(responseTimes_count):
        responseTimes_item = int(input().strip())
        responseTimes.append(responseTimes_item)

    result = countResponseTimeRegressions(responseTimes)

    print(result)
