#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
Given a sequence of nnn integers, p(1),p(2),…,p(n)p(1), p(2), p(n)p(1),p(2),…,p(n) where each element is distinct and satisfies 1≤p(x)≤n1, p(x), n1≤p(x)≤n. For each xxx where 1≤x≤n1, x, n1≤x≤n, that is xxx increments from 1 to nnn, find any integer yyy such that p(p(y))≡xp(p(y)) \equiv xp(p(y))≡x and keep a history of the values of yyy in a return array.
Example
p=[5,2,1,3,4]p = [5, 2, 1, 3, 4]p=[5,2,1,3,4]
Each value of x between 1 and 5, the length of the sequence is analyzed as follows:
x=1⇒p[3],p[4]=3⇒p[p[4]]=1x = 1 -> p[3], p[4] = 3 -> p[p[4]] = 1x=1⇒p[3],p[4]=3⇒p[p[4]]=1


x=2⇒p[2],p[2]=2⇒p[p[2]]=2x = 2 -> p[2], p[2] = 2 -> p[p[2]] = 2x=2⇒p[2],p[2]=2⇒p[p[2]]=2

x=3⇒p[4],p[5]=4⇒p[p[5]]=3x = 3 -> p[4], p[5] = 4 -> p[p[5]] = 3x=3⇒p[4],p[5]=4⇒p[p[5]]=3

x=4⇒p[5],p[1]=5⇒p[p[1]]=4x = 4 -> p[5], p[1] = 5 -> p[p[1]] = 4x=4⇒p[5],p[1]=5⇒p[p[1]]=4

x=5⇒p[1],p[3]=1⇒p[p[3]]=5x = 5 -> p[1], p[3] = 1 -> p[p[3]] = 5x=5⇒p[1],p[3]=1⇒p[p[3]]=5

The values for y are [4,2,5,1,3]


"""

def permutationEquation(p):

    result = []
    # Create a value-to-index map for fast lookup
    index_map = {value: idx + 1 for idx, value in enumerate(p)}

    for x in range(1, len(p) + 1):
        y = index_map[index_map[x]]
        result.append(y)

    return result


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input().strip())

    p = list(map(int, input().rstrip().split()))

    result = permutationEquation(p)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()