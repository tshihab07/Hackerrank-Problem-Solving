"""Problem Description: Count Number Pairs
Given a sorted array of positive integers and a target value,
count the number of pairs (i, j) where i < j and array[i] + array[j] <= target.
"""

import math
import os
import random
import re
import sys


def countAffordablePairs(prices, budget):
    left = 0
    right = len(prices) - 1
    count = 0

    while left < right:
        if prices[left] + prices[right] <= budget:
            count += (right - left)
            left += 1
        else:
            right -= 1

    return count

if __name__ == '__main__':
    prices_count = int(input().strip())

    prices = []

    for _ in range(prices_count):
        prices_item = int(input().strip())
        prices.append(prices_item)

    budget = int(input().strip())

    result = countAffordablePairs(prices, budget)

    print(result)
