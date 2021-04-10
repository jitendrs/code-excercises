"""
Write a Python program to determine whether a given year is a leap year.
"""

def leapyear(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    else:
        return False



print(leapyear(2020))