#!/bin/python3

import math
import os
import random
import re
import sys

""" Description: Flatland Space Stations" for the description "Flatland is a country with a number of cities,
some of which have space stations. Cities are numbered consecutively and each has a road of 1km length connecting it to the next city.
It is not a circular route, so the first city doesn't connect with the last city.
Determine the maximum distance from any city to its nearest space station."""


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    if len(c) == n:
        return 0  # every city has a station
    
    c.sort()
    
    # Edge cases: distance from first/last city
    max_dist = max(c[0], n - 1 - c[-1])
    
    # Check gaps between consecutive stations
    for i in range(1, len(c)):
        gap = c[i] - c[i-1]
        max_dist = max(max_dist, gap // 2)
    
    return max_dist


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    c = list(map(int, input().rstrip().split()))

    result = flatlandSpaceStations(n, c)

    fptr.write(str(result) + '\n')

    fptr.close()
