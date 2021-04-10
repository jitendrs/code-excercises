'''
There are three integers k,m,n. You have to convert the number k to m by performing the given operations:
Multiply k by n
Decrease k by 2.
Decrease k by 1.
You have to perform the above operations to convert the integer from k to m and find the minimum steps.
Note: You can perform the operations in any order.


Input : -
First-line contains the number of test cases T.
The next T line contains three space-separated integers k, m, and n.

Output : -
Print minimum no. of steps as output in a new line for each test case.
'''

def mul(k,n):
    return k * n

def red_by_2(k):
    return k - 2

def red_by_1(k):
    return k - 1


k,m,n = 3,10,2
#k,m,n = 11,6,2
steps = 0
while k != m:
        
    if k < m:
        k = k * n
    
    
    
    
    
    elif k > m:
        k = k - 2
    elif   