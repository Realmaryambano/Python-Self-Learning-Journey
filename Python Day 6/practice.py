name = "Maryam Bano"
oneName = name[0:6]  # slicing from index 0 up to 6, but **not including**, index 6
print(oneName)
twoName = name[7:11]  # slicing from index 7 up to 11, but **not including**, index 11
print(twoName)
fullName = oneName + " " + twoName  # concatenation
print(fullName)

print(name[5:5])  # empty string, because starting and ending index are the same
print(name[5:4])  # empty string, because starting index is greater than ending index
print(name[5:])    # from index 5 to the end of the string
print(name[:5])    # from the start of the string up to, but not including, index 5
print(name[:])     # the whole string
print(name[-4:-1]) # slicing using negative indices
print(name[-4:])   # from the fourth last character to the end
print(name[:-4])   # from the start of the string up to, but not including, the fourth last character
print(name[-1:])   # the last character of the string
print(name[:-1])   # from the start of the string up to, but not including, the last character
print(name[-1:-5]) # empty string, because starting index is greater than ending index
print(name[-5:-1]) # slicing using negative indices
print(name[-5:11]) # from the fifth last character up to, but not including
print(name[5:-1])  # from index 5 up to, but not including, the last character
print(name[5:-5])  # empty string, because starting index is greater than ending index
print(name[5:-4])  # from index 5 up to, but not including
print(name[5:5])   # empty string, because starting and ending index are the same
print(name[5:4])   # empty string, because starting index is greater than ending index