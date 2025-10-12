# 1. Write a program to store seven fruits in a list entered by the user.
fruits = []
for i in range(7):
    addFruit = input("Enter fruit name: ")
    fruits.append(addFruit)

print(fruits)

# or

fruits = []

f1 = input("Enter fruit name: ")
fruits.append(f1)
print(fruits)

f2 = input("Enter fruit name: ")
fruits.append(f2)
print(fruits)

f3 = input("Enter fruit name: ")
fruits.append(f3)
print(fruits)

f4 = input("Enter fruit name: ")
fruits.append(f4)
print(fruits)

f5 = input("Enter fruit name: ")
fruits.append(f5)
print(fruits)

f6 = input("Enter fruit name: ")
fruits.append(f6)
print(fruits)

f7 = input("Enter fruit name: ")
fruits.append(f7)
print("\nThe 7 fruits names are: ", fruits)