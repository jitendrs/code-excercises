# Python code for deque

from collections import deque

q = deque(['Name','age','DOB'])
print(q)

# Inserting elements in queue

d = deque([1,2,3,4,5])
d.append(8)

# printing modified deque
print(f"The deque afer appending at right is : {d}")

# using appendLeft()
d.appendleft(60)

# printing modified deque
print(f"The deque after appending at left is : {d}")