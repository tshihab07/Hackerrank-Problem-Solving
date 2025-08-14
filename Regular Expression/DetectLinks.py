""" Title: Detect HTML links
Problem Description:
Charlie has been given an assignment by his Professor to strip the links and the text name from the html pages.
A html link is of the form,

<a href="http://www.hackerrank.com">HackerRank</a>  

Where a is the tag and href is an attribute which holds the link charlie is interested in. The text name is HackerRank.
Charlie notices that the text name can sometimes be hidden within multiple tags

<a href="http://www.hackerrank.com"><h1><b>HackerRank</b></h1></a>
Here, the text name is hidden inside the tags h1 and b.

Help Charlie in listing all the links and the text name of the links.
"""

import re
import sys

data = sys.stdin.read()
pattern = r'<a\s[^>]*href\s*=\s*["\']([^"\']+)["\'][^>]*>(.*?)</a>'
matches = re.findall(pattern, data, re.DOTALL)

for url, inner in matches:
    text = re.sub(r'<[^>]+>', '', inner).strip()
    print(f"{url},{text}")