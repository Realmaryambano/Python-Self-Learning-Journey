# 3. Can we have a set with 18 (int) and '18' (str) as a value in it?
s = {18,"a","2",True}
print(s)

s = {18,"18"}
print(s) 

# {True, 18, '2', 'a'}
# {18, '18'}