""" Problem Description: Two Sum
Given an array of positive integers and a target integer,
return the indices of two elements that sum to the target or [-1, -1] if no such pair exists.
"""

#!/bin/python3

import math
import os
import random
import re
import sys


def findTaskPairForSlot(taskDurations, slotLength):
    seen = {}

    for i, duration in enumerate(taskDurations):
        needed = slotLength - duration

        if needed in seen:
            return [seen[needed], i]

        seen[duration] = i

    return [-1, -1]

if __name__ == '__main__':
    taskDurations_count = int(input().strip())

    taskDurations = []

    for _ in range(taskDurations_count):
        taskDurations_item = int(input().strip())
        taskDurations.append(taskDurations_item)

    slotLength = int(input().strip())

    result = findTaskPairForSlot(taskDurations, slotLength)

    print('\n'.join(map(str, result)))
