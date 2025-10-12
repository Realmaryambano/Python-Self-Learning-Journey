# CHAPTER 5 – PRACTICE SET
# 1. Write a program to create a dictionary of Hindi words with values as their English
# translation. Provide user with an option to look it up!

translation = {"khilona":"food",
               "aik":"one",
               "do": 2,
               "pani":"water",
               "parda":"curtain",
               "gaana":"song"}

checktrans = input("Enter the word for checking translation: ") # dictionary mai wo word mojud hona chahiye
print(translation[checktrans])