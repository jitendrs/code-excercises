 #!/usr/bin/env python3
 
"""
Python built-in types objects are as follows,
1. Numbers:
  Number can be represented in different form like Integer without precision, floating point with precision,
  complex number with imaginary parts, rationals with numerator and denominators.
"""
print("-"*80)
a = 10
print(f"variable a is integer number without precision:{a}")

print("-"*80)
b = 4.5
print(f"variable b is floating point number with precision{b}")

print("-"*80)
import math
print("Module `math` is build-in powerful tool to perform mathematical operations on numbers..")
print("for example, the value of pi can be obtained from `math.pi`",math.pi)

print("-"*80)
import random
print("Module random is used to generate random numbers...")
print(f"generated random number is {random.random()}")
print("It also used to choose numbers from given choices..")
print(f"for example,{random.choices([1,2,3,4,5])} randomly choosen from [1,2,3,4,5]")

