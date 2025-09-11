""" Problem Description:
The itertools module standardizes a core set of fast, memory efficient tools that are useful by themselves or in combination.
Together, they form an iterator algebra making it possible to construct specialized tools succinctly and efficiently in pure Python.

You are given a list of N lowercase English letters.
For a given integer K, you can select any K indices (assume 1-based indexing) with a uniform probability from the list.

Find the probability that at least one of the K indices selected will contain the letter: 'a'.
"""

from itertools import combinations

n = int(input())
letters = input().split()
k = int(input())

all_combinations = list(combinations(letters, k))
favorable = sum(1 for combo in all_combinations if 'a' in combo)
probability = favorable / len(all_combinations)

print(f"{probability:.3f}")