""" Title: Validate Properly Nested Brackets
Given a string, check if all brackets ('()', '{}', '[]') are properly matched and nested. Return 1 if valid, otherwise return 0.
"""

import math
import os
import random
import re
import sys


def areBracketsProperlyMatched(code_snippet):
    stack = []
    # Mapping of closing to opening brackets
    mapping = {')': '(', '}': '{', ']': '['}
    
    for char in code_snippet:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != mapping[char]:
                return False
    
    return len(stack) == 0

if __name__ == '__main__':
    code_snippet = input()

    result = areBracketsProperlyMatched(code_snippet)

    print(int(result))
