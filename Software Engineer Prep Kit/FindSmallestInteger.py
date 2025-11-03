#!/bin/python3

""" Problem Description:
# Find the Smallest Missing Positive Integer
Given an unsorted array of integers, find the smallest positive integer not present in the array in O(n) time and O(1) extra space.
"""

import math
import os
import random
import re
import sys


def findSmallestMissingPositive(orderNumbers):
    n = len(orderNumbers)
    
    for i in range(n):
        while 1 <= orderNumbers[i] <= n and orderNumbers[orderNumbers[i] - 1] != orderNumbers[i]:
            # Swap orderNumbers[i] to its correct position
            correct_index = orderNumbers[i] - 1
            orderNumbers[i], orderNumbers[correct_index] = orderNumbers[correct_index], orderNumbers[i]
    
    for i in range(n):
        if orderNumbers[i] != i + 1:
            return i + 1
    
    return n + 1


if __name__ == '__main__':
    orderNumbers_count = int(input().strip())

    orderNumbers = []

    for _ in range(orderNumbers_count):
        orderNumbers_item = int(input().strip())
        orderNumbers.append(orderNumbers_item)

    result = findSmallestMissingPositive(orderNumbers)

    print(result)