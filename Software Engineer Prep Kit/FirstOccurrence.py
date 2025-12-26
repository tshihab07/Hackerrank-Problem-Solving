""" Find First Occurrence
Given a sorted array of integers that may contain duplicates,
return the index of the first occurrence of a target value or -1 if not found."""

import math
import os
import random
import re
import sys


def findFirstOccurrence(nums, target):
    left, right = 0, len(nums) - 1
    first_index = -1

    while left <= right:
        mid = left + (right - left) // 2

        if nums[mid] == target:
            first_index = mid
            right = mid - 1
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return first_index

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = findFirstOccurrence(nums, target)

    print(result)
