""" Problem Description: Generate Valid Angle Bracket Sequences 
Given n, return all valid sequences of n pairs of '<' and '>' with proper nesting.
"""

import math
import os
import random
import re
import sys


def generateAngleBracketSequences(n):
    result = []

    def backtrack(current, open_count, close_count):
        if len(current) == 2 * n:
            result.append(current)
            return

        if open_count < n:
            backtrack(current + "<", open_count + 1, close_count)

        if close_count < open_count:
            backtrack(current + ">", open_count, close_count + 1)

    backtrack("", 0, 0)
    return result


if __name__ == '__main__':
    n = int(input().strip())

    result = generateAngleBracketSequences(n)

    print('\n'.join(result))
