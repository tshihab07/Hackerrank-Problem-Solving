import os
import random
import re
import sys

""" Project Description:
Sam's house has an apple tree and an orange tree that yield an abundance of fruit.
Using the information given below, determine the number of apples and oranges that land on Sam's house.

The red region denotes the house, where s is the start point, and t is the endpoint. The apple tree is to the left of the house, and the orange tree is to its right.
Assume the trees are located on a single point, where the apple tree is at point a, and the orange tree is at point b.
When a fruit falls from its tree, it lands d units of distance from its tree of origin along the x-axis.
*A negative value of d means the fruit fell d units to the tree's left, and a positive value of d means it falls d units to the tree's right. *
"""


def countApplesAndOranges(s, t, a, b, apples, oranges):
    # Write your code here
    apple_count = 0
    orange_count = 0
    
    max_length = max(len(apples), len(oranges))
    
    for idx in range(max_length):
        if idx < len(apples):
            count = apples[idx] + a
            if s <= count <= t:
                apple_count += 1
                
        if idx < len(oranges):
            count = oranges[idx] + b
            if s <= count <= t:
                orange_count += 1
    
    print(apple_count)
    print(orange_count)

    
if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    s = int(first_multiple_input[0])

    t = int(first_multiple_input[1])

    second_multiple_input = input().rstrip().split()

    a = int(second_multiple_input[0])

    b = int(second_multiple_input[1])

    third_multiple_input = input().rstrip().split()

    m = int(third_multiple_input[0])

    n = int(third_multiple_input[1])

    apples = list(map(int, input().rstrip().split()))

    oranges = list(map(int, input().rstrip().split()))

    countApplesAndOranges(s, t, a, b, apples, oranges)
