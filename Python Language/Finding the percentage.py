""" Problem Description:
The provided code stub will read in a dictionary containing key/value pairs of name:[marks] for a list of students.
Print the average of the marks array for the student name provided, showing 2 places after the decimal.

Example
marks key:value pairs are
'alpha': [20, 30, 40]
'beta': [30, 50, 70]

query_name = 'beta'
The query_name is 'beta'. beta's average score is (30 + 50 + 70) / 3 = 50.0.
"""

if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    marks_sum = 0
    count = 0
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    
    for i in student_marks[query_name]:
        marks_sum += i
        count += 1
    
    avg = marks_sum/count
    print("{:.2f}".format(avg))