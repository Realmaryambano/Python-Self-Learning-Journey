# text = "  Hello, World!  "
# name = "maryam bano"
# word = "Python"

# # 5. strip() → Removes spaces from both ends
# print(text.strip())       # Output: Hello, World!

# # 6. lstrip() → Removes spaces from the left side
# print(text.lstrip())      # Output: "Hello, World!  "

# # 7. rstrip() → Removes spaces from the right side
# print(text.rstrip())      # Output: "  Hello, World!"

# # 8. replace() → Replaces part of the string with another
# print(word.replace("Py", "My"))  # Output: Mython

# # 9. split() → Splits string into list by spaces (default) or given separator
# print(name.split())       # Output: ['maryam', 'bano']

# # 10. join() → Joins list elements into a string with a separator
# print("-".join(["a", "b", "c"]))  # Output: a-b-c

# # 12. index() → Returns index of first occurrence (error if not found)
# print(name.index("b"))    # Output: 7

# # 13. count() → Counts how many times a substring appears
# print(name.count("a"))    # Output: 3

# # 16. isalpha() → Returns True if all characters are letters
# print("Hello".isalpha())  # Output: True

# # 17. isdigit() → Returns True if all characters are digits
# print("12345".isdigit())  # Output: True

# # 18. isalnum() → Returns True if all characters are letters or digits
# print("abc123".isalnum()) # Output: True

# # 19. swapcase() → Swaps uppercase to lowercase and vice versa
# print("PyThOn".swapcase())  # Output: pYtHoN

# # 20. zfill() → Pads number with leading zeros to reach given length
# print("42".zfill(5))      # Output: 00042





# name = 'Maram Bano\'s old name was Maryam Bano but now it\'s gonna be Maryam Shakeel'
# print(name.replace("Bano","Shakeel")) # Maram Shakeel's old name was Maryam Shakeel but now it's gonna be Maryam Shakeel

# name = "Maryam Bano"
# index = name.find("no") # find print the index of the word where its located
# index1 = name.find("a") # find print the index of the 1st occurence where its located
# index2 = name.find("z") # find print -1 if its not located
# print(index)  # 9
# print(index1)  # 1
# print(index2) # -1

# name = "maryam bano"
# print(name.capitalize()) # Maryam bano - capitalize the first word
# print(name.upper()) # MARYAM BANO
# print(name.lower()) # maryam bano
# print(name.title()) # Maryam Bano


# text = """Hello
# World
# Python"""
# print(text)


# s = "Python"
# print("Py" in s)   # True
# print("Py " in s)   # Falsa
# print("py" not in s)  # True
# print("py" in s) # Falsa

# print("Hi! " * 3)  # Hi! Hi! Hi!
# s1 = "Hello"
# s2 = "World"
# print(s1 + " " + s2)  # Hello World


# s = "Hello"
# # s[0] = "h"  # ❌ Error
# s = "hello"   # ✅ Works

# city = "San Francisco"
# slice_city = city[::4]
# print(slice_city) #SFco


# text = "ProgrammingIsFun"
# slice_text = text[1:12:2]
# print(slice_text) #rgamnI

# full_name = "Alexandria Montgomery"
# slice_name = full_name[2:15:3]
# print(slice_name) #eniMt

# s = "Python"
# print(s[0:4])  # Pyth
# print(s[::2])  # Pto


# s = "Python"
# print(s[0])  # P
# print(s[-1]) # n


# s1 = 'Hello'
# s2 = "World"


# name = "Maryam Bano"
# oneName = name[0:6]  # slicing from index 0 up to 6, but **not including**, index 6
# print(oneName)

# a = int(input("Enter number to find the square of: "))
# print(f'Square of {a} is {a*a}')

# import math
# a = int(input("Enter number to find the square root: "))
# print(f'Square root of {a} is {int(math.sqrt(a))}')


# a = int(input("Enter 1st number: "))
# b = int(input("Enter 2nd number: "))
# print(f'Average of {a} and {b} is {(a+b)/2}' )


# a = 34
# b = 80
# print(f'Find out whether {a}  is greater than {b} or not: ' , a > b)



# number = input("Enter number to be divided: ")
# print("the type of variable is: " , type(number))
