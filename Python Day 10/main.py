# Initialize an empty list to store student names
students_list = []

# Loop 5 times to take input from user
for i in range(5):
    name = input("Enter student name: ")  # Take student name as input
    students_list.append(name)  # Add the name to the list

# Print the list of student names
print(f'The list of student name is: {students_list}')

# Convert the list into a tuple (because tuples are immutable like we can's add any new names in tuple through input. so we use list to append students)
students_list = tuple(students_list)

# Print the tuple of student names
print(f'The tuple of student name is: {students_list}')
