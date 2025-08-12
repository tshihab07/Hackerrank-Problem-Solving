"""
Problem SubString: In this challenge, the user enters a string and a substring.
You have to print the number of times that the substring occurs in the given string.
String traversal will take place from left to right, not from right to left.
"""

def count_str(string, substring):
    count = 0
    
    for i in range(len(string) - (len(substring)-1)):
        if string[i:].startswith(substring):
            count += 1
    
    return count


if __name__ == '__main__':
    string = input("Enter String: ")
    sub = input("Enter Substring: ")
    
    counter = count_str(string, sub)
    print(counter)