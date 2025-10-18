details = []

for i in range(3):
    name = input("Enter student name: ")
    details.append(name)

details = tuple(details)

print(type(details))
print(details)
