# 2. Write a program to fill in a letter template given below with name and date.
# letter = '''
# Dear <|Name|>,
# You are selected!
# <|Date|>
# '''

letter = '''
Dear <|Name|>,
You are selected!
<|Date|>
'''

name = input("Enter your name: ")
date = input("Enter today's date: ")
letter = letter.replace("<|Name|>", name)
letter = letter.replace("<|Date|>", date)
print(letter)



