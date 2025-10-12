# ==========================
# Creating dictionaries
# ==========================

# 1️⃣ Empty dictionary
dict1 = {}
print("Empty dictionary:", dict1)

# 2️⃣ Dictionary with values
dict2 = {
    "name": "Ali",
    "country": "India",
    "cake": "Chocolate",
    "age": 20,
    "school": "BUKC",
    "city": "Karachi"
}

# Remove a specific key and get its value
city = dict2.pop("city")   
print("\nRemoved 'city':", city)
print("Dictionary after removing 'city':", dict2)

# Remove the last inserted key-value pair
last = dict2.popitem()     
print("\nRemoved last item:", last)
print("Dictionary after popitem():", dict2)

# Access values using key or get()
print("\nAccess 'name':", dict2["name"])
print("Access 'country' using get():", dict2.get("country"))
print("Access 'food' using get():", dict2.get("food"))
print("Access 'sport' using get():", dict2.get("sport","Not exist"))


# 3️⃣ Using dict() constructor
dict3 = dict(name="Ali", age=20, city="Karachi")
print("\nDictionary using dict() constructor:", dict3)

# 4️⃣ From a list of tuples
dict4 = dict([("name", "Ali"), ("age", 20)])
print("\nDictionary from list of tuples:", dict4)
