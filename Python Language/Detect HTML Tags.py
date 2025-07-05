# Enter your code here. Read input from STDIN. Print output to STDOUT
from html.parser import HTMLParser

class MyHTMLParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print(tag)
        for attr in attrs:
            print(f"-> {attr[0]} > {attr[1]}")

# Read input
n = int(input())
html = ''
for _ in range(n):
    html += input().strip() + '\n'

# Feed parser
parser = MyHTMLParser()
parser.feed(html)