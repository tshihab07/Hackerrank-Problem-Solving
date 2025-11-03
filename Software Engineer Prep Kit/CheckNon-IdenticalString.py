#!/bin/python3

""" Problem Description: 
# Check for Non-Identical String Rotation
Given two strings s1 and s2, return 1 if s2 is a rotation of s1 but not identical to s1, otherwise return 0
"""


import math
import os
import random
import re
import sys


def isNonTrivialRotation(s1, s2):
    if len(s1) != len(s2):
        return False
    
    if s1 == s2:
        return False
    
    return s2 in s1 + s1

if __name__ == '__main__':
    s1 = input()

    s2 = input()

    result = isNonTrivialRotation(s1, s2)

    print(int(result))
