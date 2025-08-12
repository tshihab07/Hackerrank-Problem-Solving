"""
Problem - Desiginer Door Mate: Creating a pattern with a name inside it
"""
# Method - I: List Comprehensions
height = int(input("Enter Height: "))
width = height * 3
mid = height // 2

name = input("Name on The Nameplate: ")

print("\n")

pattern = [('.|.' * (2*i + 1)).center(width, '-') for i in range(mid)]

print("\n".join(pattern + [name.center(width, '-')] + pattern[::-1]))


# Method - II: Using Loops
print("\n\n")
pattern_list = []
for i in range(mid):
    pattern_list.append((".|."*(2*i + 1)).center(width, '-'))

print("\n".join(pattern_list + [name.center(width, '-')] + pattern_list[::-1]))