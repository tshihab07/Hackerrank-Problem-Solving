""" Title: Target Index Search
Given a sorted array of distinct integers and a target value, return the index of the target or -1 if not found. """

import math
import os
import random
import re
import sys


def binarySearch(nums, target):
    left, right = 0, len(nums) - 1
    
    while left <= right:
        mid = left + (right - left) // 2
        
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

if __name__ == '__main__':
    nums_count = int(input().strip())

    nums = []

    for _ in range(nums_count):
        nums_item = int(input().strip())
        nums.append(nums_item)

    target = int(input().strip())

    result = binarySearch(nums, target)

    print(result)
