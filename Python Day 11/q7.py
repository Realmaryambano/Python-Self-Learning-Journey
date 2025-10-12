# 7. If the names of 2 friends are same; what will happen to the program in problem 6?
emptyDict = {}

for i in range(4):
    name = input("Enter your name: ")
    lang = input("Enter your favourite language: ")

    emptyDict[name] = lang

print(emptyDict)

# If two friends enter the same name, the dictionary will overwrite the previous entry with the new language.