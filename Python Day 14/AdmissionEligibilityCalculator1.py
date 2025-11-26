# Admission Eligibility Calculator

age = int(input("Enter your age: "))

if age < 0:
    print("Invalid age. Age cannot be negative.")
elif age < 18:
    print("You are underage. Admission will begin once you turn 18.")
elif age <= 23:
    print("You are eligible for admission in a Bachelor's program.")
elif age <= 29:
    print("You are eligible for admission in a Master's program.")
elif age <= 39:
    print("You are eligible for admission in a PhD program.")
else:
    print("You are no longer eligible for admission at our university.")
