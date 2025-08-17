""" Title: Matching Whitespace & Non-Whitespace Character 
Task: You have a test string S. The task is to match the pattern XXxXXxXX
Here, x denotes whitespace characters and X denotes the non-whitespace characters
"""

Regex_Pattern = r"\S{2}\s\S{2}\s\S{2}"

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())