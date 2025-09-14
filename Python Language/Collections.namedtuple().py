from collections import namedtuple

N = int(input())
columns = input().split()
Student = namedtuple('Student', columns)

total_marks = 0

for _ in range(N):
    data = input().split()
    student = Student(*data)
    total_marks += int(student.MARKS)

print(f"{total_marks / N:.2f}")