fruits = ["apple", "banana", "cherry", "date", "elderberry"]
fruits.remove("apple")   # remove by value
# ['banana', 'cherry', 'date', 'elderberry']


last = fruits.pop()      # remove last item
# ['banana', 'cherry', 'date']

fruits.pop(0)            # remove by index
# ['cherry', 'date']

del fruits[0]            # delete by index
# ['date']

fruits.clear()           # empty the list
# []

numbers = [1, 2, 3, 2, 4]
print(numbers.index(2))   # 1 (first index of 2)
print(numbers.count(2))   # 2 (how many times 2 appears)
print(3 in numbers)       # True (membership check)
print(len(numbers))       # 5 (length of the list)


a = [1, 2]
b = [3, 4]
c = a + b           # [1, 2, 3, 4]
# or
a.extend(b)         # modifies a to [1, 2, 3, 4]
#  here c and a.extend(b) achieve the same result
