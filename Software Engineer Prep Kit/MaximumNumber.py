""" Title: Maximum Number of Non-Overlapping Intervals
Given an array of intervals where each interval has a start and end time, return the maximum number of non-overlapping intervals."""

import math
import os
import random
import re
import sys


def maximizeNonOverlappingMeetings(meetings):
    if not meetings:
        return 0
    
    meetings_sorted = sorted(meetings, key=lambda x: x[1])
    
    count = 0
    last_end = float('-inf')
    
    for start, end in meetings_sorted:
        if start >= last_end:
            count += 1
            last_end = end
    
    return count

if __name__ == '__main__':
    meetings_rows = int(input().strip())
    meetings_columns = int(input().strip())

    meetings = []

    for _ in range(meetings_rows):
        meetings.append(list(map(int, input().rstrip().split())))

    result = maximizeNonOverlappingMeetings(meetings)

    print(result)
