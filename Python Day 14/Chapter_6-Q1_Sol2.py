# Program to find the greatest of four numbers

a = int(input("Enter 1st number: "))
b = int(input("Enter 2nd number: "))
c = int(input("Enter 3rd number: "))
d = int(input("Enter 4th number: "))

greatest = a 

if b > greatest:
    greatest = b

if c > greatest:
    greatest = c

if d > greatest:
    greatest = d

print(f"{greatest} is the greatest")
