'''
animals = ["lion","tiger","elephant","deer"]

answer = [[x.lower(),x.title(),len(x)] for x in animals]
print(answer)
'''

fruits = ["apple", "banana", "cherry", "kiwi", "mango"]

newlist = [x for x in fruits if "a" in x]

print(newlist)