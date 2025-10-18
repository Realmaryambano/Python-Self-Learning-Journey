# -------------------------------
# LIST REVISION WITH COMPARISON
# -------------------------------

# A list can store multiple types, and is mutable
fruits = ["apple", "banana", "cherry"]
print("Original List:", fruits)

# Lists are ordered
print("First item:", fruits[0])

# Mutable → you can modify elements
fruits[1] = "orange"
print("After change:", fruits)

# Add and remove
fruits.append("grapes")
fruits.remove("apple")
print("After add/remove:", fruits)

# Iteration
for fruit in fruits:
    print("Fruit:", fruit)

# Compare with tuple
fruits_tuple = ("apple", "banana", "cherry")
# fruits_tuple[0] = "kiwi"  # ❌ Error: tuple is immutable

# Compare with set
fruits_set = {"apple", "banana", "cherry", "apple"}
# Set removes duplicates and has no order
print("Set:", fruits_set)

# Compare with dictionary
fruits_dict = {"a": "apple", "b": "banana"}
print("Dictionary:", fruits_dict)

# Compare with frozenset
frozen = frozenset(["apple", "banana", "cherry"])
# frozen.add("grape")  # ❌ Error: cannot modify frozen set
