""" Title: Matching Start & End
Task: You have a test string S. The task is to match the pattern Xxxxx.
S must start with a digit X and end with . symbol
S should be 6 characters long only
"""

Regex_Pattern = r"^\d\w{4}\.$"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())