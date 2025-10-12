student = {"name": "Ali", "age": 20, "grade": "A"}

# Keys only
for key in student:
    print(key) # we can use any variable name instead of key

# Values only
for value in student.values(): # we can use any var name instead of value but values is a method name of dictionary thats accessible through .
    print(value)

# Keys and values
for key, value in student.items():
    print(key, value)
# here key and value is a simple variable name that can we changed but items is a method name used to access both keys and values
