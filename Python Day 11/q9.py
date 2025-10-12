# 9. Can you change the values inside a list which is contained in set S? 
# s = {8, 7, 12, "Harry", [1,2]} 

s = {8, 7, 12, "Harry", [1,2]} 
print(s)

''' In Python, sets are collections of unique elements that are unordered and mutable. However, sets can only contain hashable (immutable) elements, such as numbers, strings, and tuples. Mutable types like lists, dictionaries, or other sets cannot be added because they can change and would break the internal hash table. If you try to include a list, Python raises a TypeError: unhashable type. Also, sets automatically remove duplicates, so adding the same value multiple times has no effect. While sets preserve insertion order in Python 3.7+, they do not support indexing like lists or tuples.'''