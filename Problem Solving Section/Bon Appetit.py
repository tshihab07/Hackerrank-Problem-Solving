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

def bonAppetit(bill, k, b):
    
    rest_items = sum(bill[:k]) + sum(bill[k+1:])
    actual_bill = rest_items // 2
    
    if actual_bill < b:
        print(b - actual_bill)
    
    elif actual_bill == b:
        print("Bon Appetit")
        

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    bill = list(map(int, input().rstrip().split()))

    b = int(input().strip())

    bonAppetit(bill, k, b)