username = input("Enter username: ")
length = len(username)

RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
RESET = "\033[0m"

if length < 10:
    print(RED + "Less than 10 characters" + RESET)
elif length == 10:
    print(GREEN + "Exactly 10 characters" + RESET)
else:
    print(YELLOW + "More than 10 characters" + RESET)
