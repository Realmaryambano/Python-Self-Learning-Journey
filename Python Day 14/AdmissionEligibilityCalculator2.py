# Admission eligibility calculator code 2

age = int(input("Enter your age: "))
if (age < 0 ):
    print("Invalid age")
elif(age < 18 ):
    print("You are underage")
elif(age == 18):
    print("You are still 18. admission will begin once you're above 18")
elif(age>18 and age<24):
    print("You are eligible for admission in bachelors")
elif(age>=24 and age < 30):
    print("You are eligible for admission in masters")
elif(age>=30 and age <= 40):
    print("You are eligible for PHD")
else:
    print("You are no longer eligible for admission at our university")
