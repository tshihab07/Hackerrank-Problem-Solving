""" Problem Description: Given a non-decreasing array of integers and an integer K,
remove in-place any element that is within K of the previous kept element and return the new length.
Use constant extra space and single pass with two pointers."""

#!/bin/python3

import math
import os
import random
import re
import sys


def debounceTimestamps(timestamps, K):
    if not timestamps:
        return 0

    write = 1                   # index of next position to write a valid element

    for read in range(1, len(timestamps)):
        if timestamps[read] - timestamps[write - 1] > K:
            timestamps[write] = timestamps[read]
            write += 1

    return write

if __name__ == '__main__':
    timestamps_count = int(input().strip())

    timestamps = []

    for _ in range(timestamps_count):
        timestamps_item = int(input().strip())
        timestamps.append(timestamps_item)

    K = int(input().strip())

    result = debounceTimestamps(timestamps, K)

    print(result)
