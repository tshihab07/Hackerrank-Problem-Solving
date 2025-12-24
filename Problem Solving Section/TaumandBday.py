import math
import os
import random
import re
import sys

""" Problem Description:
Taum is planning to celebrate the birthday of his friend, Diksha.
There are two types of gifts that Diksha wants from Taum: one is black and the other is white.
To make her happy, Taum has to buy b black gifts and  white gifts.

The cost of each black gift is bc units.
The cost of every white gift is wc units.
The cost to convert a black gift into white gift or vice versa is z units.
Determine the minimum cost of Diksha's gifts.
"""

def taumBday(b, w, bc, wc, z):
    cost_black = min(bc, wc + z)  # Either buy black directly or buy white and convert
    cost_white = min(wc, bc + z)  # Either buy white directly or buy black and convert
    
    return b * cost_black + w * cost_white

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    t = int(input().strip())

    for t_itr in range(t):
        first_multiple_input = input().rstrip().split()

        b = int(first_multiple_input[0])

        w = int(first_multiple_input[1])

        second_multiple_input = input().rstrip().split()

        bc = int(second_multiple_input[0])

        wc = int(second_multiple_input[1])

        z = int(second_multiple_input[2])

        result = taumBday(b, w, bc, wc, z)

        fptr.write(str(result) + '\n')

    fptr.close()
