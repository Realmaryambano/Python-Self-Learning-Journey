# # empty tuple
# empty_tuple = ()

# # tuple with values
# fruits = ("apple", "banana", "cherry")

# # tuple with mixed data types
# mixed = (10, "text", 3.14, True)

# # single-element tuple (important)
# single = ("apple",)  # must include comma because if we forget it then python will treat it at single variable and not as tuple


# fruits = ("apple", "banana", "cherry", "mango")

# print(fruits[0])    # first element
# print(fruits[-1])   # last element
# print(fruits[1:3])  # slicing → ('banana', 'cherry')


# fruits = ("apple", "banana", "cherry")

# # fruits[1] = "orange"  # error: tuples are immutable

# new_fruits = fruits + ("orange",)
# print(new_fruits)

# numbers = (1, 2, 3, 4, 5)

# print(len(numbers))      # number of elements
# print(min(numbers))      # smallest element
# print(max(numbers))      # largest element
# print(sum(numbers))      # sum of all elements
# print(numbers.count(2))  # count occurrences
# print(numbers.index(4))  # find index of element


# fruits = ("apple", "banana", "cherry")

# for fruit in fruits:
#     print(fruit)

# nested = (("a", 1), ("b", 2), ("c", 3))
# print(nested[1][1])  # access inner element → 2

# # packing
# person = ("Alice", 25, "Engineer")

# # unpacking
# name, age, job = person
# print(name)
# print(age)
# print(job)
