import math
import os
import random
import re
import sys

def howManyGames(p, d, m, s):
    # Return the number of games you can buy
    games = 0
    current_price = p
    total_spent = 0
    
    while total_spent + current_price <= s:
        total_spent += current_price
        games += 1
        current_price = max(current_price - d, m)
    
    return games


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    first_multiple_input = input().rstrip().split()

    p = int(first_multiple_input[0])

    d = int(first_multiple_input[1])

    m = int(first_multiple_input[2])

    s = int(first_multiple_input[3])

    answer = howManyGames(p, d, m, s)

    fptr.write(str(answer) + '\n')

    fptr.close()
