from functools import reduce
# Write your code here
N  = int(input())
A = list(map(int,input().split(' ')))
ele = []

index = 0
while index < N:
    if reduce(lambda x,y: x + y,[x for i, x in enumerate(A) if i != index]) % 7 == 0:
        ele.append(A[index])
    index += 1
print(A.index(min(ele)))
