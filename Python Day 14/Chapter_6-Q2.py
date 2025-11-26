# 2. Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# Program to check pass/fail with 40% total and 33% in each subject

marks = []

for i in range(3):
    n = int(input(f"Enter marks for subject {i+1}: "))
    marks.append(n)

average = sum(marks) / 3

# Check total percentage first
# if average < 40:
#     print("Failed (Total percentage is less than 40%)")

# Check individual subject condition
if marks[0] < 33 and marks[1] < 33 and marks[2] < 33:
    print("Failed (One or more subjects have less than 33%)")

else:
    print("Passed")

print(f"Your average marks are: {average}")
