# 6. Create an empty dictionary. Allow 4 friends to enter their favorite language as
# value and use key as their names. Assume that the names are unique.

emptyDict = {}

for i in range(4):
    name = input("Enter your name: ")
    lang = input("Enter your favourite language: ")

    emptyDict[name] = lang

print(emptyDict)
