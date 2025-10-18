# list vs tuple comparison

# list - mutable
my_list = ["apple", "banana", "cherry"]
my_list[1] = "orange"
my_list.append("grape")
print("List after changes:", my_list)

# tuple - immutable
my_tuple = ("apple", "banana", "cherry")
# my_tuple[1] = "orange"  # error
new_tuple = my_tuple + ("grape",)
print("Tuple after adding new value:", new_tuple)

# tuple allows duplicates
dup_tuple = (1, 2, 2, 3)
print("Tuple with duplicates:", dup_tuple)

# accessing tuple elements
print("Second element:", my_tuple[1])

# iteration
for item in my_tuple:
    print("Tuple item:", item)
