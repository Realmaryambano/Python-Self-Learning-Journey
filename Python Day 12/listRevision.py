# Creating a list
my_list = [10, 20, 30, 20, "Python", True]

print("Original list:", my_list)

# 1. Accessing items (Indexing)
print("First item:", my_list[0])

# 2. Changing items (Mutable)
my_list[1] = 99
print("After changing second item:", my_list)

# 3. Adding items
my_list.append("New Item")
print("After append:", my_list)

# 4. Removing items
my_list.remove(20)  # removes first 20
print("After remove:", my_list)

# 5. Slicing
print("Slice [1:4]:", my_list[1:4])

# 6. Length of list
print("Length:", len(my_list))



# Tuple: immutable list
my_tuple = (10, 20, 30)

# Set: unordered, no duplicates
my_set = {10, 20, 20, 30}  # becomes {10, 20, 30}

# Frozen Set: immutable set
my_fset = frozenset([10, 20, 20, 30])

# Dictionary: key-value pairs
my_dict = {"a": 10, "b": 20, "c": 30}
