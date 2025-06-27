#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'climbingLeaderboard' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY ranked
#  2. INTEGER_ARRAY player
#

def climbingLeaderboard(ranked, player):
    # Write your code here
    # Step 1: Remove duplicates and sort in descending order
    unique_ranks = sorted(set(ranked), reverse=True)

    results = []
    index = len(unique_ranks) - 1  # Start from the lowest rank

    for score in player:
        # Step 2: Move up while player score is >= ranked score
        while index >= 0 and score >= unique_ranks[index]:
            index -= 1
        # Step 3: Player's rank is index+2 (because rank is 1-based, and index moved past)
        results.append(index + 2)

    return results


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    ranked_count = int(input().strip())

    ranked = list(map(int, input().rstrip().split()))

    player_count = int(input().strip())

    player = list(map(int, input().rstrip().split()))

    result = climbingLeaderboard(ranked, player)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
