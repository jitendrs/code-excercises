#!/usr/bin/env python3

'''
With a given integral number n, write a program to generate a dictionary that contains (i, i x i) 
such that i is an integral number between 1 and n (both included). 
and then the program should print the dictionary.Suppose the following input is supplied to the program: 8
Then, the output should be:

{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}
'''
n = int(input("Please enter number: "))
print({x: x * x for x in range(1,n+1)})