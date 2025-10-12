person = {"name": "Ali", "age": 20}

print(person["age"])
# print(person["city"]) this will generate key error and the rest program wont be able to run
print(person["name"])        # Ali
print(person.get("age"))     # 20
print(person.get("city", "Not Found in the dictionary"))  # Default value if key missing

person["city"] = "Karachi"  # Add new key
person["age"] = 21          # Update existing key

print(person) # {'name': 'Ali', 'age': 21, 'city': 'Karachi'}
