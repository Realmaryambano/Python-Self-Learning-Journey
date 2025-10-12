# name1 = {"haya", "ayesha", "areeba","fatima"}
# name2 = {"haya", "ayesha", "areeba","muskan","manahil","haya"} # Order may change every time you run

# # print(name1)
# # print(name2)

# # All unique elements from A & B
# print(name1 | name2)
# # or
# print(name1.union(name2))

# # Common elements
# print(name1 & name2)
# # or
# print(name1.intersection(name2))

# # Elements in A or B but not both
# print(name1 ^ name2)
# # or
# print(name1.symmetric_difference(name2))


# A = {1, 2, 3}
# B = {3, 4, 5}
# print(A | B)  # {1,2,3,4,5}
# print(A & B)  # {3}
# print(A - B)  # {1,2}
# print(A ^ B)  # {1,2,4,5}
# print(A.isdisjoint(B))

fset = frozenset([1, 2, 3])
print(fset)
