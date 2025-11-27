# 4. Write a program to find whether a given username contains less than 10 characters or not.

username = input("Enter your username: ")
count = len(username)

if count < 10:
    print(f"The username '{username}' contains less than 10 characters")
elif count == 10:
    print(f"The username '{username}' contains 10 characters")
else:
    print(f"The username '{username}' contains more than 10 characters")

