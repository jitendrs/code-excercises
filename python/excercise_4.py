"""
Write a Python program to get the current time in Python.
Sample Format :  13:19:49.078205
"""
from datetime import datetime as dt

print(dt.now().time())
print(dt.strftime(dt.now(), "%H:%M:%s"))
