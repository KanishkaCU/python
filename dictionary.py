n = int(input())
students = {}
for i in range(n):
    name = input("name")
    marks = list(map(int, input("Enter marks: ").split()))
    students[name]=marks
print(students)

maxi = max(students.values())
mini = min(students.values())
print(maxi,mini)

for name in students:
    avg = sum(students[name])/len(students[name])
print(avg)


