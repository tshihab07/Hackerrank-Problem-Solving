""" Problem Description:
# Check Palindrome by Filtering Non-Letters
Given a string containing letters, digits, and symbols,
determine if it reads the same forwards and backwards when considering only alphabetic characters (case-insensitive).
"""

import math
import os
import random
import re
import sys


def isAlphabeticPalindrome(code):
    left, right = 0, len(code) - 1
    
    while left < right:
        # skip non-letter characters from left
        while left < right and not code[left].isalpha():
            left += 1
        # skip non-letter characters from right
        while left < right and not code[right].isalpha():
            right -= 1
        
        # compare case-insensitively
        if code[left].lower() != code[right].lower():
            return False
        
        left += 1
        right -= 1
        
    return True

if __name__ == '__main__':
    code = input()

    result = isAlphabeticPalindrome(code)

    print(int(result))
