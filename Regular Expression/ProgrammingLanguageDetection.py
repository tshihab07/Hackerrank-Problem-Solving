""" Title: Building a Smart IDE: Programming Language Detection
Description: We are trying to hack together a smart programming IDE.
Help us build a feature which auto-detects the programming language, given the source code.
There are only three languages which we are interested in "auto-detecting": Java, C and Python.

We will provide you with links to a few short or medium size programs for Java, C and Python.
In case you aren't familiar with some of these languages,
these samples will help you make observations about the lexical structure and syntax of these programming languages.
These sample programs are only for your manual inspection. You cannot read or access these sample-programs from the code you submit.

After this, you will be provided with tests, where you are provided the source code for programs - or partial code snippets,
but you do not know which language they are in. For each test, try to detect which language the source code is in.

You might benefit from using regular expressions in trying to detect the lexical structure and syntax of the programs provided.
"""

import sys
import re

def detect_language(code_lines):
    code = '\n'.join(code_lines)

    java_patterns = [
        r'import\s+java\.', 
        r'public\s+class',
        r'System\.out\.println',
        r'static\s+void\s+main'
    ]

    c_patterns = [
        r'#include\s*<.*>',
        r'printf\s*\(',
        r'scanf\s*\(',
        r'int\s+main\s*\('
    ]

    python_patterns = [
        r'def\s+\w+\s*\(',
        r'print\s+',
        r'import\s+\w+',
        r'"""',
        r"'''"
    ]

    def count_matches(patterns):
        return sum(len(re.findall(p, code)) for p in patterns)

    java_score = count_matches(java_patterns)
    c_score = count_matches(c_patterns)
    python_score = count_matches(python_patterns)

    # Debug (comment out in final submission)
    # print(f"Java score: {java_score}, C score: {c_score}, Python score: {python_score}")

    scores = {'Java': java_score, 'C': c_score, 'Python': python_score}

    # Choose max score language; if tie, priority order Java > C > Python
    max_score = max(scores.values())
    candidates = [lang for lang, score in scores.items() if score == max_score]

    for lang in ['Java', 'C', 'Python']:
        if lang in candidates:
            return lang

# Read multiple lines until EOF
code_lines = []
for line in sys.stdin:
    code_lines.append(line.rstrip('\n'))

language = detect_language(code_lines)
print(language)
