import os

""" Problem Description:
A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget.
Given price lists for keyboards and USB drives and a budget, find the cost to buy them.
If it is not possible to buy both items, return -1.

Example:
b = 60
keyboards = [40, 50, 60]
drives = [5, 8, 12]
The person can buy a 40 keyboards + 12 USB Drives = 52, or a 50 keyboards + 8 USB Drives.
Choose the latter as the more expensive option and return 58.
"""


def getMoneySpent(keyboards, drives, b):
    # Write your code here.

    max_price = -1
    for k in keyboards:
        for d in drives:
            total = k + d
            if total <= b and total > max_price:
                max_price = total
    return max_price


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    bnm = input().split()

    b = int(bnm[0])

    n = int(bnm[1])

    m = int(bnm[2])

    keyboards = list(map(int, input().rstrip().split()))

    drives = list(map(int, input().rstrip().split()))

    #
    # The maximum amount of money she can spend on a keyboard and USB drive, or -1 if she can't purchase both items
    #

    moneySpent = getMoneySpent(keyboards, drives, b)

    fptr.write(str(moneySpent) + '\n')

    fptr.close()
