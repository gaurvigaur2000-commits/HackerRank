stu = int(input("Enter no. of students: "))
sub = int(input("Enter no. of subjects: "))
names = input("Enter student names: ").split()
dict1 = {}

print("Enter marks of each student: ")

for name in names:
    grades = list(map(int, input().split()))
    dict1[name] = grades

print("Student record: ", dict1)

name = input("Enter student name to get average: ")

if name in dict1.keys():
    grades = dict1[name]
    avg = sum(grades)/sub
    print(f"Average: {avg:.2f}")
else:
    print("Name not found!!")