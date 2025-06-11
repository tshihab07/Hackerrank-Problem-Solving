import math
import os
import random
import re
import sys

""" Project Description:
Given an array of bird sightings where every element represents a bird type id, determine the id of the most frequently sighted type.
If more than 1 type has been spotted that maximum amount, return the smallest of their ids.

Example - 
arr = [1, 1, 2, 2, 3]
There are two each of types 1 and 2, and one sighting of type 3. Pick the lower of the two types seen twice: type 1.

"""

def migratoryBirds(arr):
    # Write your code here
    max_sight = 0
    
    for item in set(arr):
        count = arr.count(item)
        if max_sight < count:
            max_sight = count
            bird_type = item
        
        elif count == max_sight and bird_type > item:
            bird_type = item
    
    return bird_type
            



if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    arr_count = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    result = migratoryBirds(arr)

    fptr.write(str(result) + '\n')

    fptr.close()
