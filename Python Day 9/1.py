person = {"name": "Ali", "age": 20}

person["city"] = "Karachi"  # Add new key
person["age"] = 21          # Update existing key

print(person) # {'name': 'Ali', 'age': 21, 'city': 'Karachi'}

del person["age"]           # Delete key
print(person)
print("\n\n")


city = person.pop("city")   # Remove key and return its value
print(city)
print(person)


print("\n\n")
last = person.popitem()     # Removes the last inserted key-value pair
print(last)
print(person)
person.clear()              # Clear all items
print(person)
