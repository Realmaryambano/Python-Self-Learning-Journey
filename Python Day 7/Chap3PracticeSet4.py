# 4. Replace the double space from problem 3 with single spaces.

text = input("Enter a string: ")
result = "  " in text
print("Is double space found in the string?",result )

if result == True:
    replaced_text = text.replace("  ", " ")
    print("New string = ", replaced_text)
else:
    print("No double space found in the string.")
