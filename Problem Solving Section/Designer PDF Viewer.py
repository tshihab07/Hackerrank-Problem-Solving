import os

""" Problem Description:
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle.
In this PDF viewer, each word is highlighted independently. For example:
There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25.
There will also be a string.
Using the letter heights given, determine the area of the rectangle highlight in mm2 assuming all letters are 1mm wide.
"""

def designerPdfViewer(h, word):
    max_height = 0
    for char in word:
        index = ord(char) - ord('a')  # Get index in h
        height = h[index]
        if height > max_height:
            max_height = height

    return max_height * len(word)


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)

    fptr.write(str(result) + '\n')

    fptr.close()