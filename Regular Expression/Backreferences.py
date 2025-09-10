""" Title: Backreferences To Failed Groups
Task:
You have a test string S.
Your task is to write a regex which will match S, with the following condition(s):

- S consists of 8 digits.
- S may have "-" separator such that string S gets divided in 4 parts, with each part having exactly two digits. (Eg. 12-34-56-78)
"""

Regex_Pattern = r"^(\d{2})(-?)(\d{2})\2(\d{2})\2(\d{2})$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())