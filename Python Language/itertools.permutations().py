""" Problem Description:
itertools.permutations(iterable[, r])
This tool returns successive r length permutations of elements in an iterable.
If r is not specified or is None, then r defaults to the length of the iterable, and all possible full length permutations are generated.
"""

import itertools

first_input = input().split()
txt = first_input[0]
length = int(first_input[1])

perm = sorted(itertools.permutations(txt, length))

for el in perm:
    print("".join(el))
