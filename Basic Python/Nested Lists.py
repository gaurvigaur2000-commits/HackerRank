students = int(input("Enter no. of students: "))
names = list(input("Names of students: ").split())
grades = list(map(float, input("Grades: ").split()))
stu_list = [[names, grades] for names, grades in zip(names, grades)]

print(stu_list)

unique_grades = sorted(set([grades for names, grades in stu_list]))
final = sorted([names for names, grades in stu_list if grades == unique_grades[1]])

print(*final)