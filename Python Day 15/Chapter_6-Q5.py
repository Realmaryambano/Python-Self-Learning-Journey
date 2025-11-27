# 5. Write a program which finds out whether a given name is present in a list or not.
names_list = []

num = int(input("Enter number of names: "))
for i in range(num):
    name = input(f"{i+1}. Enter name in list: ").title()
    names_list.append(name)

searchName = input("Enter the name you want to search: ").title()

if searchName in names_list:
    print(f"{searchName} is present in the list.")
else:
    print(f"{searchName} is not present in the list.")
