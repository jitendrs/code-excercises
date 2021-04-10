"""
Regualar expression methods
"""

import re


# re.match method


grp = re.match("Hello", "Hello")
if grp is not None:
    print(grp.group())

m = re.match("Hello", "how Hello are you")
if m is not None:
    print(m.group())


print(re.match("Hello", "Hello").group())


# re.search method

m = re.search("abc", "IsTHere any abcHere abc")
if m is not None:
    print(m.group())


# Matching more than one string

bt = 'bat|bet|bit'

m = re.match(bt,'bit')
if m is not None:
    print(m.group())

m = re.match(bt,'This is not here its at bit of the string')
if m is not None:
    print(m.group())


# Matching single character
anyend = '.end'
m = re.match(anyend,'hend')
if m is not None:
    print(m.group())

