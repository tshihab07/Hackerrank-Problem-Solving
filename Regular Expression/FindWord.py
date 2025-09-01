""" Problem Description:
We define a word as a non-empty maximum sequence of characters that can contain only
lowercase letters, uppercase letters, digits and underscores '_' (ASCII value 95).
Maximum sequence means that the word has to be immediately preceeded by a character not allowed to occur in a word
or by the left boundary of the sentence, and it has to be immediately followed by a character not allowed to occur in a word or
by the right boundary of the sentence.
Given N sentences and T words, for each of these words, find the number of its occurences in all the N sentences.
"""

import re

n = int(input().strip())
sentences = [input().strip() for _ in range(n)]

t = int(input().strip())
words = [input().strip() for _ in range(t)]

text = "\n".join(sentences)

for w in words:
    # match word exactly using \b boundaries
    pattern = r"\b" + re.escape(w) + r"\b"
    matches = re.findall(pattern, text)
    print(len(matches))
