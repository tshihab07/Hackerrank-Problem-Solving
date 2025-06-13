#!/bin/python3

import math
import os
import random
import re
import sys

""" Problem Description:
Two friends Anna and Brian, are deciding how to split the bill at a dinner.
Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion.
You must determine if his calculation is correct.

For example, assume the bill has the following prices: bill = [2, 4, 6]. Anna declines to eat item k = bill[2], which costs 6.
If Brian calculates the bill correctly,  Anna will pay (2 + 4) / 2 = 3. If he includes the cost of bill[2], he will calculate (2 + 4 + 6) / 2 = 6.
In the second case, he should refund 3 to Anna.
"""

def dayOfProgrammer(year):
    # Write your code here
    if year == 1918:
        return "26.09.1918"
    elif (year < 1918 and year % 4 == 0) or \
         (year > 1918 and (year % 400 == 0 or (year % 4 == 0 and year % 100 != 0))):
        return f"12.09.{year}"
    else:
        return f"13.09.{year}"

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    year = int(input().strip())

    result = dayOfProgrammer(year)

    fptr.write(result + '\n')

    fptr.close()
