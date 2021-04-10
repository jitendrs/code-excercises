"""
Write a Python program to convert a string to datetime. Go to the editor
Sample String : Jan 1 2014 2:43PM
Expected Output : 2014-07-01 14:43:00
"""

from datetime import datetime as dt


s = "Jan 1 2014 2:43PM"
print(dt.strptime(s,"%b %d %Y %H:%M%p"))