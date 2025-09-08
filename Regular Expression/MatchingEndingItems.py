"""Title: Matching Ending Items
Tasks:
Write a RegEx to match a test string, S, under the following conditions: 

- S should consist of only lowercase and uppercase letters (no numbers or symbols). 
- S should end in s.
"""


# \b indicates the boundary of the pattern
Regex_Pattern = r'\b[a-zA-Z]*s\b'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())