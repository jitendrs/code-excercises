# A python program to show different ways to create Counter
from collections import Counter

print("\n---- Sequence Items-----")
# with sequence of items
print(Counter(['B','A','D','E','F','A','B','C']))

# with dictionary
print("\n---- Dict-----")
print(Counter({'A':3, 'B':5,'C':20,'C':1,'C':5}))


print("\n----keyword arguments-----")
# with keyword arguments
print(Counter(A=3,B=5,C=2))

# To update counter
print("\n----------------------")
coun = Counter()
coun.update([1,2,3,1,5,6,5,7,8,10,2])
print(coun[10])
for e in coun.elements():
    print(e)
print(coun)

print("\n--------------------------")
# subtract counter elements
c1 = Counter(A=4,B=2,C=10)
c2 = Counter(A=14,B=20,C=3)
c1.subtract(c2)
print(c1)
