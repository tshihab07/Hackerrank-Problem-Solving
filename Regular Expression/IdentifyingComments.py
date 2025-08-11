""" Title: Building a Smart IDE: Identifying comments
Problem Description: Jack wants to build an IDE on his own.
Help him build a feature which identifies the comments, in the source code of computer programs.
Assume, that the programs are written either in C, C++ or Java.
The commenting conventions are displayed here, for your convenience.
At this point of time you only need to handle simple and common kinds of comments.
You don't need to handle nested comments, or multi-line comments inside single comments or single-comments inside multi-line comments.

Your task is to write a program, which accepts as input, a C or C++ or Java program and outputs only the comments from those programs.
Your program will be tested on source codes of not more than 200 lines.
"""

import re
import re
import sys

code = sys.stdin.read()
comments = re.findall(r'//.*|/\*[\s\S]*?\*/', code)

for comment in comments:
    if comment.startswith('//'):
        print(comment)
    else:
        # Remove leading whitespace from each line of multi-line comment
        print('\n'.join(line.lstrip() for line in comment.split('\n')))