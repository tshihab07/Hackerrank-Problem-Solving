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