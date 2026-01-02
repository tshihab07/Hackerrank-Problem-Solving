""" Title: Min-Tracking Stack Implementation
Implement a stack that supports push, pop, top, and getMin operations in O(1) time, where getMin returns the minimum element."""

import math
import os
import random
import re
import sys


def processCouponStackOperations(operations):
    main_stack = []
    min_stack = []
    output = []

    for op in operations:
        if op.startswith("push"):
            # Extract integer
            x = int(op.split()[1])
            main_stack.append(x)
            if not min_stack or x <= min_stack[-1]:
                min_stack.append(x)
            else:
                min_stack.append(min_stack[-1])  # maintain current min
        
        elif op == "pop":
            if main_stack:
                main_stack.pop()
                min_stack.pop()
        
        elif op == "top":
            if main_stack:
                output.append(main_stack[-1])
        
        elif op == "getMin":
            if min_stack:
                output.append(min_stack[-1])

    return output

if __name__ == '__main__':
    operations_count = int(input().strip())

    operations = []

    for _ in range(operations_count):
        operations_item = input()
        operations.append(operations_item)

    result = processCouponStackOperations(operations)

    print('\n'.join(map(str, result)))
