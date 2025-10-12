# 2. Write a program to accept marks of 6 students and display them in a sorted
# manner.
marks = []
for i in range(6):
    storingMarks = int(input("Enter marks of student: "))
    marks.append(storingMarks)
print(marks)
marks.sort()
print("Marks after sorting: ", marks)

