""" Problem Description:
ABCXYZ company has up to 100 employees.
The company decides to create a unique identification number (UID) for each of its employees.
The company has assigned you the task of validating all the randomly generated UIDs. A valid UID must follow the rules below:
1. It must contain at least 2 uppercase English alphabet characters.
2. It must contain at least 3 digits (0-9).
3. It should only contain alphanumeric characters.
4. It should not contain any spaces.
5. No character should repeat.
6. The UID should be exactly 10 characters long.
"""

def is_valid_uid(uid):
    if len(uid) != 10:
        return False
    if not uid.isalnum():
        return False
    if len(set(uid)) != len(uid):  # check for repetition
        return False
    if sum(c.isupper() for c in uid) < 2:
        return False
    if sum(c.isdigit() for c in uid) < 3:
        return False
    return True

# Input reading
n = int(input())
for _ in range(n):
    uid = input().strip()
    print("Valid" if is_valid_uid(uid) else "Invalid")