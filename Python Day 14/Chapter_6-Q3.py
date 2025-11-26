# 3. A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

comment = input("Enter a comment: ").lower()

if "make a lot of money" in comment:
    print("This is a spam comment")
elif "buy now" in comment:
    print("This is a spam comment")
elif "subscribe this" in comment:
    print("This is a spam comment")
elif "click this" in comment:
    print("This is a spam comment")
else:
    print("This is not a spam comment")
