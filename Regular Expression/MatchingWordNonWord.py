""" Title: Matching Word & Non-Word Character
Task: You have a test string S. The task is to match the pattern xxxXxxxxxxxxxxXxxx
Here, x denotes word characters and X denotes the non-word characters
"""

Regex_Pattern = r"\w{3}\W\w+\W\w{3}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())