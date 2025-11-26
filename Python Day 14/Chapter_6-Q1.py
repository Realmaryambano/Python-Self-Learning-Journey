# Program to find the greatest of four numbers

numbers = []  # list to store the numbers

for i in range(4): # range 4 means 0,1,2,3 means it starts from 0, and length is 4
    n = int(input(f"Enter number {i+1}: "))
    numbers.append(n)

greatest = max(numbers)  # find the maximum number
print(f"The numbers you entered are: {numbers}")
print(f"The greatest number is: {greatest}")
