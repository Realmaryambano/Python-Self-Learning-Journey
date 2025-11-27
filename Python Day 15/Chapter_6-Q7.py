# 7. Write a program to find out whether a given post is talking about “Harry” or not.

post = input("Write a post: ").lower()

if "harry" in post:
    print(f'The post is about Harry \n{post.title()}')
else:
    print(f'The post is not about Harry \n{post.title()}')
