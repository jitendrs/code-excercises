"""
1. Write a Python script to display the various Date Time formats - Go to the editor
a) Current date and time
b) Current year
c) Month of year
d) Week number of the year
e) Weekday of the week
f) Day of year
g) Day of the month
h) Day of week
"""

from datetime import datetime as dt
import calendar

now = dt.now()

print("Current date time: ", now)
print("Current year: ",now.strftime("%Y"))
print("Current month: ",now.strftime("%B"))
print("Current week of the year: ",now.strftime("%W"))
print("Weekday of the week: ",now.strftime("%w"))
print("Day of year: ",now.strftime("%j"))
print("Day of the month: ",now.strftime("%d"))
print("Day of week: ",now.strftime("%A"))


