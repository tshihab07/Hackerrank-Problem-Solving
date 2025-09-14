from collections import Counter

# Read number of shoes
X = int(input())

# Read the list of shoe sizes and create a Counter
shoe_sizes = list(map(int, input().split()))
shoes = Counter(shoe_sizes)

# Read number of customers
N = int(input())

total_earned = 0

# Process each customer
for _ in range(N):
    size, price = map(int, input().split())
    if shoes[size] > 0:
        total_earned += price
        shoes[size] -= 1

print(total_earned)