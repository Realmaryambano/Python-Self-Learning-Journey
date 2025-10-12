my_list = [10, "hello", 3.14, True]
print(my_list)
# [10, 'hello', 3.14, True]

empty_list = []                 # empty list
numbers = [1, 2, 3, 4, 5]        # list of integers
mixed = [1, "Python", 3.5]       # mixed types
nested = [[1, 2], [3, 4]]        # nested (list of lists)

fruits = ["apple", "banana", "cherry"]

print(fruits[0])   # apple (first item)
print(fruits[-1])  # cherry (last item)
print(fruits[1:3]) # ['banana', 'cherry'] (slice)

# Python does not throw an error in slicing if the stop index goes beyond the list length. It just stops at the end.

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"   # change banana to orange
print(fruits)
# ['apple', 'orange', 'cherry']
fruits.append("mango")      # add at the end
fruits.insert(1, "kiwi")    # add at index 1
print(fruits)
# ['apple', 'kiwi', 'orange', 'cherry', 'mango']
