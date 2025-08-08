""" Title: Matching Digits & Non-Digit Characters 
Task: You have a test string S. The task is to match the pattern xxXxxXxxxx
Here, x denotes digit characters and X denotes the non-digit character
"""

Regex_Pattern = r"\d{2}\D\d{2}\D\d{4}"	# Do not delete 'r'.

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())