# ==========================
# Working with Sets in Python
# ==========================

# 1️⃣ Empty set
set1 = set()
print("Empty set:", set1)

# 2️⃣ Set with elements
set2 = {1, 2, 3, 4}
print("Set with elements:", set2)

# 3️⃣ Creating a set from a list (duplicates removed automatically)
set3 = set([1, 2, 2, 3, 3])
print("Set from list (duplicates removed):", set3)  # {1, 2, 3}

# 4️⃣ Adding elements
my_set = {1, 2}
print("\nOriginal set:", my_set)

# Add a single element
my_set.add(3)
print("After adding 3:", my_set)

# Add multiple elements (duplicates ignored)
my_set.update([4, 5, 3, 3, 2])
print("After updating with [4,5,3,3,2]:", my_set)

# Output at this point:
# {1, 2}
# {1, 2, 3}
# {1, 2, 3, 4, 5}

# 5️⃣ Removing elements
# Remove element (error if not found)
my_set.remove(2)
print("After removing 2:", my_set)

# Remove element safely (no error if not found)
my_set.discard(10)
print("After discarding 10 (not present):", my_set)

# Remove a random element
my_set.pop()
print("After popping a random element:", my_set)

# Clear all elements
my_set.clear()
print("After clearing the set:", my_set)
