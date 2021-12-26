number_of_students = int(input("Enter number of students: "))
increment = 1

student_marks = []

while increment <= number_of_students:
    print(f"=======Student {increment}=====")
    for mark in range(1):
        nep = int(input("Enter np mark: "))
        eng = int(input("Enter eng mark: "))
        mat = int(input("Enter mat mark: "))
        sic = int(input("Enter sic mark: "))
        pop = int(input("Enter pop mark: "))
        data = [nep, eng, mat, sic, pop]
        student_marks.append(data)

    increment += 1

total_student_mark = []
for student in student_marks:
    total = 0
    for mk in student:
        total += mk

    total_student_mark.append(total)

x = 1
for tt in total_student_mark:
    pre = tt / 5
    division = ''

    if pre > 30 and pre < 45:
        division += "pass"
    elif pre > 45 and pre < 60:
        division += 'second'

    elif pre > 60 and pre < 75:
        division += 'first'

    elif pre > 75 and pre < 100:
        division += 'top'

    else:
        print('test')

    print(f"Student: {x} Total: {tt} Pre: {pre} Division: {division}")
    x += 1
