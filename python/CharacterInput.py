"""
Program that asks user to ennter their name and their age. Print out a message addressed to them that tells them the year that they will turn 100 year old.
"""

from datetime import  datetime

name = input("Enter your name: ")
age = int(input("Enter your age: "))
now = datetime.now()
print("{0}, you are turning to 100 in {1}".format(name, str(now.year + (100 - age))))
      