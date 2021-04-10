#!/usr/bin/env python3

'''
Write a program which can compute the factorial of a given numbers.
The results should be printed in a comma-separated sequence on a single line.
Suppose the following input is supplied to the program: 8 Then, the output should be:40320
'''

def recursive_fact(n):
    
    if n == 1 or n == 0:
        return 1
    return n * recursive_fact(n-1) 

def while_fact(n):
    
    fact = 1
    i = 1
    while i <= n:
        fact = fact * i
        i = i + 1
    print(f"Factorial with while loop: {fact}")

def for_fact(n):
    
    fact = 1
    for i in range(1,n+1):
        fact = fact * i
    print(f"Factorial with for loop: {fact}")



num = int(input("Please enter number to compute factorial: "))
print("Recursive factorial: ",recursive_fact(num))
while_fact(num)
for_fact(num)
