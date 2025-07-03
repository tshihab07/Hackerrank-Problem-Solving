""" Problem Description:
itertools.combinations(iterable, r)
This tool returns the r length subsequences of elements from the input iterable.
Combinations are emitted in lexicographic sorted order.
So, if the input iterable is sorted, the combination tuples will be produced in sorted order.
"""

import itertools

input_seq = input().split()

seq = input_seq[0].upper()
k = int(input_seq[1])
sort_seq = sorted(seq)

for i in range(1, k+1):
    for j in itertools.combinations(sort_seq, i):
        print("".join(j))
