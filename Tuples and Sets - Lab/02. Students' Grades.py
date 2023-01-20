n = int(input())
student_strings = [input() for _ in range(n)]
    # 'Peter 5.20',
    # 'Mark 5.50',
    # 'Peter 3.20',
    # 'Mark 2.50',
    # 'Alex 2.00',
    # 'Mark 3.46',
    # 'Alex 3.00',
# ]
# n = 4
# student_string = [
# 'Scott 4.50',
# 'Ted 3.00',
# 'Scott 5.00',
# 'Ted 3.66'
# ]
# n = 5
# student_string = [
# 'Lee 6.00',
# 'Lee 5.50',
# 'Lee 6.00',
# 'Peter 4.40',
# 'Kenny 3.30'
# ]


def avg(values):
    return sum(values) / len(values)


students_grades = {}

for student_string in student_strings:
    student, grade_string = student_string.split(' ')
    grade = float(grade_string)
    if student not in students_grades:
        students_grades[student] = []

    students_grades[student].append(grade)
for student, grades in students_grades.items():
    grades_formatted = ' '.join(f'{grade:.2f}' for grade in grades)
    grade_avg = avg(grades)
    grades_avg_formatted = f'{grade_avg:.2f}'
    print(f'{student} -> {grades_formatted} (avg: {grades_avg_formatted})')
