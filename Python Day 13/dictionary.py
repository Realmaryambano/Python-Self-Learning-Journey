# # empty dictionary
# my_dict = {}

# # dictionary with data
# student = {"name": "Alice", "age": 20, "grade": "A"}

# # using dict() constructor
# person = dict(name="John", age=25, job="Engineer")

# # nested dictionary
# students = {
#     "student1": {"name": "Alice", "age": 20},
#     "student2": {"name": "Bob", "age": 22}
# }


# storing student data
student = {
    "name": "Ali",
    "age": 21,
    "subjects": ["Math", "Science", "English"],
    "grades": {"Math": "A", "Science": "B+", "English": "A-"}
}

print("Student Name:", student["name"])
print("Math Grade:", student["grades"]["Math"])


# dictionary comparison with list, tuple, and set

# list
fruits_list = ["apple", "banana", "cherry"]
print("List example:", fruits_list[1])

# tuple
fruits_tuple = ("apple", "banana", "cherry")
print("Tuple example:", fruits_tuple[1])

# set
fruits_set = {"apple", "banana", "cherry"}
print("Set example:", fruits_set)  # unordered

# dictionary
fruits_dict = {"a": "apple", "b": "banana", "c": "cherry"}
print("Dictionary example:", fruits_dict["b"])  # accessed by key



students = {
    "student1": {"name": "Alice", "age": 20},
    "student2": {"name": "Bob", "age": 22}
}

print(students["student1"]["name"])



countries = {
    "country1" : {"Pakistan": "Islamabad", "Language":"Urdu"}
}

print(countries["country1"]["Language"])



student = {"name": "Alice", "age": 20, "grade": "A"}

print(student["name"])   # access value using key
print(student.get("age"))  # safer way to access


student = {"name": "Alice", "age": 20}

# adding a new key-value pair
student["grade"] = "A"

# modifying existing value
student["age"] = 21

print(student)








student = {"name": "Alice", "age": 21, "grade": "A"}

# remove a specific key
student.pop("grade")

# remove last inserted key
student.popitem()

# remove by del statement
del student["age"]

# remove all items
student.clear()

print(student)







person = {"name": "John", "age": 25, "city": "Lahore"}

print(len(person))             # total key-value pairs
print(person.keys())           # returns all keys
print(person.values())         # returns all values
print(person.items())          # returns all key-value pairs
print("name" in person)        # check if key exists










person = {"name": "John", "age": 25, "city": "Lahore"}

for key in person:
    print("Key:", key, "Value:", person[key])

# or using items()
for key, value in person.items():
    print(key, "→", value)









original = {"a": 1, "b": 2}
copy_dict = original.copy()

copy_dict["c"] = 3
print("Original:", original)
print("Copy:", copy_dict)
