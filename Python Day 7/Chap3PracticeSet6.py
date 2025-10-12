# Write a Python program that takes a string as input and replaces all instances of multiple spaces (two or more spaces in a row) with a single space. The program should work no matter if the string has 2, 3, 5, or more spaces.

text = input("Enter a text: ")
text = text.split()
text = (" ".join(text))

print(text)