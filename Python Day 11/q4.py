# 4. What will be the length of following set s:
# s = set()
# s.add(20)
# s.add(20.0)
# s.add('20') # length of s after these operations?

s = set()
s.add(20)      # int, kept
s.add(20.0)    # float, same value as 20 → ignored
s.add(20.44)   # float, unique → kept
s.add(21.0)    # float, unique → kept
s.add(21)      # int, same as 21.0 → ignored
s.add('20')    # string → unique → kept

print(s)
# Output: {20, 20.44, 21.0, '20'}
