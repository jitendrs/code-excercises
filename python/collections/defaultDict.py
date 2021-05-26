# A program to demonstrate default dict in python collection

from collections import defaultdict

# Defining the dict
d = defaultdict(int)

L = [1,2,3, 4, 2, 4, 1, 2]

# Iterate through the list for keeping the count
for i in L:
    # The default value is 0
    # so there is no need to enter the first key
    d[i] += 1
print(d)

print("----------------")
d = defaultdict(list)
for i in range(5):
    d[i].append(i)

print("Dictionary with value as list:")
print(d)