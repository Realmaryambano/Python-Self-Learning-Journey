# empty set
my_set = set()     # must use set(), {} creates an empty dictionary

# set with values
fruits = {"apple", "banana", "cherry"}

# set with mixed data types
mixed = {1, 2.5, "hello", True}

# duplicates are removed automatically
numbers = {1, 2, 2, 3, 4, 4}
print(numbers)   # output: {1, 2, 3, 4}






fruits = {"apple", "banana", "cherry"}
for fruit in fruits:
    print(fruit)








fruits = {"apple", "banana"}

# adding elements
fruits.add("cherry")        # add a single element
fruits.update(["mango", "grape"])  # add multiple elements
print(fruits)

# removing elements
fruits.remove("apple")      # removes element; gives error if not found
fruits.discard("kiwi")      # no error if element not found
removed = fruits.pop()      # removes random element
print(fruits)

# clear all elements
fruits.clear()
print(fruits)  # output: set()





A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# union → combines both sets (no duplicates)
print(A | B)         # {1, 2, 3, 4, 5, 6}
print(A.union(B))    # same result

# intersection → common elements
print(A & B)         # {3, 4}
print(A.intersection(B))  # same

# difference → elements in A but not in B
print(A - B)         # {1, 2}
print(A.difference(B))

# symmetric difference → elements in A or B but not both
print(A ^ B)         # {1, 2, 5, 6}
print(A.symmetric_difference(B))




fruits = {"apple", "banana", "cherry"}

print("apple" in fruits)    # True
print("mango" not in fruits) # True



A = {1, 2, 3}
B = A.copy()

B.add(4)
print("A:", A)
print("B:", B)


numbers = frozenset([1, 2, 3, 4])
# numbers.add(5)  # error: frozenset has no add() method
print(numbers)




# list vs set vs frozenset comparison

# list - allows duplicates and order matters
my_list = [1, 2, 2, 3]
print("List:", my_list)

# set - removes duplicates and is unordered
my_set = {1, 2, 2, 3}
print("Set:", my_set)

# frozenset - same as set but immutable
my_frozenset = frozenset([1, 2, 3])
print("Frozenset:", my_frozenset)

# attempting modification
# my_frozenset.add(4)  # error: frozenset object has no attribute 'add'




# finding unique items from a list
numbers = [1, 2, 2, 3, 4, 4, 5]
unique_numbers = set(numbers)
print(unique_numbers)

# performing operations on sets
even = {2, 4, 6, 8}
odd = {1, 3, 5, 7, 9}

all_numbers = even.union(odd)
print("All numbers:", all_numbers)

common = even.intersection(odd)
print("Common numbers:", common)

difference = even.difference(odd)
print("Numbers only in even:", difference)

