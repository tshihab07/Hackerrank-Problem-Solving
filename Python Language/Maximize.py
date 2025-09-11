from itertools import product

# Read K and M
K, M = map(int, input().split())

# Read K lists; ignore first number (count) and take rest as elements
lists = []
for _ in range(K):
    line = list(map(int, input().split()))
    # First element is N_i, rest are the numbers
    lists.append(line[1:])

# Generate Cartesian product of all lists
max_result = 0
for combo in product(*lists):
    # Compute sum of squares mod M
    s = sum(x * x for x in combo) % M
    if s > max_result:
        max_result = s

print(max_result)