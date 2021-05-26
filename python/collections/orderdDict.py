# A python program to demonstrate working if OrderedDict

from collections import OrderedDict

d = {'a':1,'b':2,'c':4,'d':5}
print(f"------\nThis is Dictionary {d}")
for key,value in d.items():
    print(f"{key} : {value}")

print("\nThis is OrderedDict")
ord = OrderedDict()
ord['a'] = 1
ord['c'] = 3
ord['b'] = 4
ord['d'] = 5
print("Before Deleting")
for key, value in ord.items():
    print(key,value)
# deleting element
ord.pop('a')

# Re-inserting the same
ord['a'] = 50

print("\nAfter re-inserting")
for key, value in ord.items():
    print(key,value)
