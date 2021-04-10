#!/usr/bin/env python3

'''
Define a class which has at least two methods:

getString: to get a string from console input
printString: to print the string in upper case.
Also please include simple test function to test the class methods.
'''

class Demo:
    
    def __init__(self):
        self.s = ""
    
    def getString(self) -> None:
        self.s = input()
    
    def printString(self) -> None:
        print(self.s.upper())

ss = Demo()
ss.getString()
ss.printString()