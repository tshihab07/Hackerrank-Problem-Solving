""" Title: Matching One Or More Repetitions
Tasks:
You have a test string S.
Your task is to write a regex that will match S using the following conditions:

S should begin with 1 or more digits.
After that, S should have 1 or more lowercase letters.
S should end with 1 or more uppercase letters
"""

Regex_Pattern = r'^\d+[A-Z]+[a-z]+$'	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())