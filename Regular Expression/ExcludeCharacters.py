""" Title: Excluding Specific Characters

Task: You have a test string S.
The task is to write a regex that will match S with following conditions:

- S must be of length: 6
- First character: Should not be a digit (0-9).
- Second character: Should not be a lowercase vowel. 
- Third character: Should not be b, c, D or F.
- Fourth character: Should not be a whitespace character.
- Fifth character: Should not be a uppercase vowel.
- Sixth character: Should not be a . or , symbol.

"""

Regex_Pattern = r'^[^\d][^aeiou][^bcDF][^\s][^AEIOU][^.,]$'

import re

print(str(bool(re.search(Regex_Pattern, input()))).lower())