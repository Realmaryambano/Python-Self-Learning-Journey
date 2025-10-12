'''
MINI PROJECT – CHATGPT 🎯 STUDENT MARKS MANAGER (BEGINNER PROJECT)
Question:
1.	Ask the user for the number of students.
2.	Take input for each student’s name and marks.
3.	Store marks in a list and student names in a tuple.
4.	Display all students with their marks.
5.	Show:
o	Highest marks
o	Lowest marks
o	Average marks
6.	Use string methods to format the output (like .title(), .upper()).
7.	Use typecasting where needed.
8.	Add comments and escape sequences for formatting output.
'''

welcome = "Welcome to Students Marks Manager \n"
print(welcome.upper())
stdNum = int(input("How many students are there? "))

# first we will use as list, later we will convert to tupe as append, add methods etc aren't applicable on tuples
stdNames = []
stdMarks = []

for i in range(stdNum):
    inputName = input("Enter student name: ").title()
    stdNames.append(inputName)

    inputMarks = int(input("Enter student marks: "))
    stdMarks.append(inputMarks)

# here we converted list into tuple
stdNames = tuple(stdNames)
print("\nxxxxxxxxxxxxxxx  RESULT  xxxxxxxxxxxxxxxxxxxx")
print("Student Names: ", stdNames)
print("Student Marks: ", stdMarks)

for i in range(stdNum):
    print("\nHighest Marks is ", max(stdMarks)) #for highest marks
    print("Lowest Marks: ", min(stdMarks)) #for lowest marks
    print("Average Marks: ", round((sum(stdMarks)/stdNum),2)) #for average

