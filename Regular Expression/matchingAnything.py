""" Problem: Matching Anything but a Newline """

regex_pattern = r"^(.{3}\.?){4}$"    # Do not delete 'r'.

import re
import sys

test_string = input()

match = re.match(regex_pattern, test_string) is not None

print(str(match).lower())